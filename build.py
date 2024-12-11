# pylint: disable=invalid-name, line-too-long, missing-module-docstring
from argparse import ArgumentParser
from typing import Optional, Iterable
from time import sleep
from zipfile import ZipFile
import os.path
import platform
import shlex
import sys
from file_utils import mkdir, remove
from library_manager import LibraryManager
from options import Options

try:
    from build_utils import (
        add_path,
        cmake,
        command_exists,
        run_fg,
        make,
        make_install,
        ninja,
        require_commands,
        path_fixer,
        configure,
        meson,
    )
    from plumbum import local
except ModuleNotFoundError:
    print("Install required module with `pip install -r requirements.txt`")
    sys.exit(1)


# Set up constants
DOWNLOAD_RETRY_DELAY = 3
DOWNLOAD_RETRY_ATTEMPTS = 3

# Pseudographics
BOLD_SEPARATOR = "======================================="
ITALIC_SEPARATOR = "---------------------------------------"


def clean_all(release_dir: str, target_dir: str) -> None:
    """
    Clean all build file

    Parameters
    ----------
    release_dir: str
        Release directory
    target_dir: str
        Target directory

    Returns
    -------
    None
    """
    print("Cleaning started")
    remove(release_dir)
    remove(target_dir)
    print("Cleaning finished")


def lookahead(iterable: Iterable) -> tuple:
    """
    Lookahead function

    Parameters
    ----------
    iterable: Iterable
        Iterable value

    Returns
    -------
    tuple
    """
    it = iter(iterable)
    for value in it:
        try:
            yield value, next(it)
        except StopIteration:
            yield value, False


def print_lines(*strings) -> None:
    """
    Print strings line by line

    Parameters
    ----------
    *strings
        List of string

    Returns
    -------
    None
    """
    to_print = ""
    for line, has_more in lookahead(strings):
        to_print = to_print + line + ("\n" if has_more else "")
    print(to_print)


def print_header(*strings) -> None:
    """
    Print strings with italic separator and line by line

    Parameters
    ----------
    *strings
        List of string

    Returns
    -------
    None
    """
    to_print = strings + (ITALIC_SEPARATOR,)
    print_lines(*to_print)


def print_block(*strings) -> None:
    """
    Print strings with bold separator and line by line

    Parameters
    ----------
    *strings
        List of string

    Returns
    -------
    None
    """
    to_print = strings + (BOLD_SEPARATOR,)
    print_lines(*to_print)
    print()


class Builder:
    """
    Class to build ffmpeg
    """

    def __init__(self, options: Options):
        self._options = options
        self._old_ldflags = None
        self.__dir_data = {
            "target_dir": path_fixer(options.target_dir),
            "release_dir": path_fixer(options.release_dir),
            "bin_dir": path_fixer(os.path.join(options.release_dir, options.bin_dir)),
            "pkg_config_path": path_fixer(
                os.path.join(options.release_dir, "lib", "pkgconfig")
            ),
        }

        self.__library_mgr = LibraryManager()
        self.__library_mgr.init(options)

        ffmpeg_obj = self.__library_mgr.get_library("ffmpeg")
        if self.is_mac:
            ffmpeg_obj.add_configuration_params("--enable-videotoolbox")
        ffmpeg_obj.add_configuration_params(*shlex.split(options.extra_ffmpeg_args))
        if options.extra_libs:
            ffmpeg_obj.add_configuration_params(f"--extra-libs={options.extra_libs}")

    @property
    def target_dir(self) -> str:
        """
        Returns
        -------
        str
            Return target dir
        """
        return self.__dir_data["target_dir"]

    @property
    def release_dir(self) -> str:
        """
        Returns
        -------
        str
            Return release dir
        """
        return self.__dir_data["release_dir"]

    @property
    def bin_dir(self) -> str:
        """
        Returns
        -------
        str
            Return binary dir
        """
        return self.__dir_data["bin_dir"]

    @property
    def pkg_config_path(self) -> str:
        """
        Returns
        -------
        str
            Return pkg config path
        """
        return self.__dir_data["pkg_config_path"]

    @property
    def is_windows(self) -> bool:
        """
        Returns
        -------
        bool
        """
        return platform.system() == "Windows"

    @property
    def is_linux(self) -> bool:
        """
        Returns
        -------
        bool
        """
        return platform.system() == "Linux"

    @property
    def is_mac(self) -> bool:
        """
        Returns
        -------
        bool
        """
        return platform.system() == "Darwin"

    def __configuration_wrapper(self, lib_name: str):
        """
        Handle the library configuration

        Parameters
        ----------
        lib_name : str
            Library name
        """
        library_obj = self.__library_mgr.get_library(lib_name)
        if library_obj.has_own_configuration:
            library_obj.custom_configure()
            return
        if library_obj.configuration == "meson":
            meson(
                self.release_dir,
                *library_obj.configure_params,
                silent=self._options.silent,
            )
            library_obj.post_configure()
            ninja(self._options.threads, silent=self._options.silent)
            return
        if library_obj.configuration == "configure":
            configure(
                self.release_dir,
                *library_obj.configure_params,
                silent=self._options.silent,
            )
        elif library_obj.configuration == "cmake":
            cmake(
                self.release_dir,
                *library_obj.configure_params,
                silent=self._options.silent,
            )
        library_obj.post_configure()
        make(self._options.threads, silent=self._options.silent)
        make_install(silent=self._options.silent)

    def __build_library(self, lib_name: str, is_dependency=False) -> None:
        """
        This function will handle the build process

        Parameters
        ----------
        lib_name: str
            Library name
        is_dependency: bool (default False)
            If the library is needed by other library
        silent: bool (default False)
            Verbose or not

        Returns
        -------
        None
        """
        library_obj = self.__library_mgr.get_library(lib_name)
        if not library_obj.is_needed() and not is_dependency:
            return
        library_obj.pre_dependency()
        if library_obj.dependencies:
            for dependency in library_obj.dependencies:
                if not self.__library_mgr.get_library(dependency).is_already_build():
                    self.__build_library(dependency, is_dependency=True)

        self.download(*library_obj.download_params)  # pylint: disable = E1120
        lib_build_dir = os.path.join(self.target_dir, library_obj.folder_name)
        if not os.path.isdir(lib_build_dir):
            mkdir(lib_build_dir)
        with local.cwd(lib_build_dir):
            library_obj.pre_configure()
            self.__configuration_wrapper(lib_name)
        library_obj.post_install()
        library_obj.mark_as_built()

    def build(self) -> None:
        """
        Function to start building

        Parameters
        ----------
        slavery_mode: bool (default False)
            Is slavery mode
        build_static_ffmpeg: bool (default False)
            Is build static ffmpeg

        Returns
        -------
        None
        """
        extra_cflags = f"-I{self.release_dir}/include {self._options.extra_cflags}"
        extra_ldflags = f"-L{self.release_dir}/lib {self._options.extra_ldflags}"

        print_header("Building process started")
        mkdir(self.target_dir)
        mkdir(self.release_dir)
        add_path(self.bin_dir)

        with local.env(
            CFLAGS=f"{local.env.get('CFLAGS', '')} {extra_cflags}",
            LDFLAGS=f"{local.env.get('LDFLAGS', '')} {extra_ldflags}",
            PKG_CONFIG_LIBDIR=f"{self.release_dir}/lib/pkgconfig",
        ):
            for library in self._options.targets:
                self.__build_library(library)

        print_block()
        print_block(
            f"Finished: {self.release_dir}/bin/ffmpeg",
            "You can check correctness of this build by running: "
            f"{self.release_dir}/bin/ffmpeg -version",
            "Study the protocols list carefully (e.g, look for rtmps): "
            f"{self.release_dir}/bin/ffmpeg -protocols",
            "Enable it temporary in the command line by running: "
            f"export PATH={self.release_dir}/bin:$PATH",
        )

    def download(self, url: str, dest_name: str, alternative_dir: Optional[str] = None):
        """
        Function to download file

        Parameters
        ----------
        url: str
            Download url
        dest_name: str
            File name
        alternative_dir: Optional[str]
            Custom dir name when extract
        """
        download_path = self.target_dir

        if alternative_dir is not None:
            download_path = os.path.join(download_path, alternative_dir)
            mkdir(download_path)

        base_path = os.path.join(download_path, dest_name)
        if os.path.exists(base_path):
            print(f"Source file already downloaded: {url}")
            return

        print(f"Downloading {url}")
        successful_download = False
        for _ in range(DOWNLOAD_RETRY_ATTEMPTS):
            if run_fg("curl", "--insecure", "-L", "--silent", "-o", base_path, url):
                successful_download = True
                break
            print(
                f"Downloading failed: {url}. Retrying in {DOWNLOAD_RETRY_DELAY} seconds"
            )
            sleep(DOWNLOAD_RETRY_DELAY)

        if not successful_download:
            print(f"Failed to download multiple times: {url}")
            sys.exit(1)
        print(f"Successfuly downloaded: {url}")

        if ".tar" in dest_name:
            if run_fg(
                "tar",
                "-xvf",
                path_fixer(base_path),
                "-C",
                path_fixer(download_path),
                silent=True,
            ):
                return
            print(f"Failed to extract {dest_name}")
            sys.exit(1)
        elif ".zip" in dest_name:
            with ZipFile(base_path) as myzip:
                myzip.extractall(download_path)
            return
        raise Exception


def main() -> None:
    """
    Program Entry Point
    """
    parser = ArgumentParser(description="Build your own FFmpeg")
    parser.add_argument(
        "-j",
        "--jobs",
        metavar="int",
        action="store",
        dest="jobs",
        type=int,
        help="Number of parallel jobs",
        default=1,
    )
    parser.add_argument(
        "-b", "--build", action="store_true", dest="build_mode", help="Run build"
    )
    parser.add_argument(
        "-c",
        "--clean",
        action="store_true",
        dest="clean_mode",
        help="Clean build temp file",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        dest="silent_mode",
        help="Disable build debug",
    )
    parser.add_argument(
        "--targets",
        action="store",
        dest="targets",
        help="Comma-separated targets for building (empty = build all)",
    )
    parser.add_argument(
        "--exclude-targets",
        action="store",
        dest="exclude_targets",
        help="Don't build these",
    )
    parser.add_argument(
        "--extra-cflags",
        metavar="string",
        dest="extra_cflags",
        help="Build extra CFLAGS",
        default="",
    )
    parser.add_argument(
        "--extra-ldflags",
        metavar="string",
        dest="extra_ldflags",
        help="Build extra LDFLAGS",
        default="",
    )
    parser.add_argument(
        "--extra-libs",
        metavar="string",
        dest="extra_libs",
        help="FFmpeg extra LIBS",
        default="",
    )
    parser.add_argument(
        "--extra-ffmpeg-args",
        metavar="string",
        dest="ffmpeg_args",
        help="Extra FFmpeg argument",
        default="",
    )
    parser.add_argument(
        "--target-dir", metavar="dir", default="targets", help="Target directory"
    )
    parser.add_argument(
        "--release-dir", metavar="dir", default="release", help="Release directory"
    )
    parser.add_argument(
        "--disable-ffplay",
        dest="disable_ffplay",
        action="store_true",
        help="Disable building ffplay",
        default=False,
    )
    parser.add_argument(
        "--static-ffmpeg",
        dest="static_ffmpeg",
        action="store_true",
        help="Build static ffmpeg (-static, etc)",
        default=False,
    )
    parser.add_argument(
        "--use-nonfree-libs",
        dest="nonfree",
        action="store_true",
        help="Use non-free libraries",
        default=False,
    )
    parser.add_argument(
        "--use-system-build-tools",
        dest="default_tools",
        action="store_true",
        help="Use cmake, nasm, yasm, pkg-config that installed on system",
        default=True,
    )
    args = parser.parse_args()

    targets = [
        "cmake",
        "ffnvcodec",
        "gmp",
        "gnutls",
        "libaom",
        "libass",
        "libbluray",
        "libdav1d",
        "libfdk-aac",
        "libfontconfig",
        "libfreetype",
        "libfribidi",
        "libgme",
        "libkvazaar",
        "libmp3lame",
        "libogg",
        "libopus",
        "libopencore",
        "libopenh264",
        "libopenjpeg",
        "libsdl",
        "libshine",
        "libsoxr",
        "libsrt",
        "libsvtav1",
        "libtheora",
        "libvidstab",
        "libvmaf",
        "libvorbis",
        "libvpx",
        "libx264",
        "libx265",
        "libxvid",
        "libzimg",
        "nasm",
        "openssl",
        "pkg-config",
        "yasm",
        "zlib",
        "ffmpeg-msys2-deps",
        "ffmpeg",
    ]
    # Check if user specify specific targets
    targets = (
        [_ for _ in args.targets.split(",") if _ in targets]
        if args.targets is not None
        else targets
    )
    # Check if user exclude some targets
    targets = (
        [x for x in targets if x not in args.exclude_targets.split(",")]
        if args.exclude_targets is not None
        else targets
    )
    # Remove cmake, yasm, nasm, and pkg-config from targets if user dont wanna compile it
    targets = (
        [x for x in targets if x not in ("cmake", "pkg-config", "nasm", "yasm")]
        if args.default_tools
        else targets
    )
    if not args.nonfree:
        for target in ("libfdk-aac", "openssl"):
            if target in targets:
                targets.remove(target)

    elif args.nonfree:
        if "gnutls" in targets:
            targets.remove("gnutls")

    if args.disable_ffplay and "libsdl" in targets:
        targets.remove("libsdl")

    if any(_ in targets for _ in ("libopenh264", "libdav1d")):
        if not (bool(command_exists("meson") and command_exists("ninja"))):
            print(
                "In order to build libopenh264 or libdav1d, you must install meson and ninja in your system"
            )
            sys.exit(1)

    print_header("Processing targets:")
    print_block(str(targets))

    if args.build_mode:
        require_commands(
            "autoconf",
            "curl",
            "gperf",
            "libtoolize",
            "make",
            "tar",
            *["cmake", "nasm", "yasm", "pkg-config"] if args.default_tools else [],
        )
        opts = Options(
            targets=targets,
            threads=args.jobs,
            silent=args.silent_mode,
            target_dir=args.target_dir,
            release_dir=args.release_dir,
            extra_cflags=args.extra_cflags,
            extra_ldflags=args.extra_ldflags,
            extra_libs=args.extra_libs,
            extra_ffmpeg_args=args.ffmpeg_args,
            static_ffmpeg=args.static_ffmpeg,
            nonfree_build=args.nonfree,
        )
        Builder(opts).build()

    if args.clean_mode:
        clean_all(args.target_dir, args.release_dir)

    print("FFmpeg build success")


if __name__ == "__main__":
    main()
