#pylint: disable=invalid-name, line-too-long, missing-module-docstring
from typing import Optional
LIBRARIES={
    "cmake":{
        "download_opts": ["https://cmake.org/files/v3.15/cmake-3.15.4.tar.gz", "cmake-3.15.4.tar.gz"],
        "folder_name": "cmake-3.15.4"
    },
    "ffmpeg":{
        "configure_opts": [
            "--pkg-config-flags=--static",
            "--extra-libs=-lm",
            "--disable-doc",
            "--disable-debug",
            "--disable-shared",
            "--disable-ffprobe",
            "--enable-static",
            "--enable-gpl",
            "--enable-version3",
            "--enable-runtime-cpudetect",
            "--enable-avfilter",
            "--enable-filters"
            ],
        "download_opts": ["https://ffmpeg.org/releases/ffmpeg-5.1.1.tar.xz",
             "ffmpeg-5.1.1.tar.xz"],
        "folder_name": "ffmpeg-5.1.1"
    },
    "ffmpeg-msys2-deps":{
        "download_opts": ["https://codeload.github.com/olegchir/ffmpeg-windows-deps/zip/master",
             "ffmpeg-windows-deps-master.zip"],
        "folder_name": "ffmpeg-windows-deps-master"
    },
    "gmp":{
        "configure_opts": ["--disable-shared", "--enable-static"],
        "download_opts": ["https://gmplib.org/download/gmp/gmp-6.2.1.tar.xz",
            "gmp-6.2.1.tar.xz"],
        "folder_name": "gmp-6.2.1"
    },
    "gnutls":{
        "configure_opts": ["--disable-shared", "--enable-static", "--without-p11-kit"],
        "dependencies": ["gmp", "libtasn1", "libunistring", "nettle"],
        "download_opts": ["https://www.gnupg.org/ftp/gcrypt/gnutls/v3.6/gnutls-3.6.16.tar.xz",
            "gnutls-3.6.16.tar.xz"],
        "folder_name": "gnutls-3.6.16"
    },
    "harfbuzz":{
        "configure_opts": ["--enable-static", "--disable-shared", "--with-freetype=yes"],
        "dependencies": ["libfreetype"],
        "download_opts": ["https://github.com/harfbuzz/harfbuzz/releases/download/5.3.1/harfbuzz-5.3.1.tar.xz",
            "harfbuzz-5.3.1.tar.xz"],
        "folder_name": "harfbuzz-5.3.1"
    },
    "libaom":{
        "configuration": "cmake",
        "configure_opts": ["-DENABLE_TESTS=0", "-DENABLE_NASM=on"],
        "download_opts": ["https://aomedia.googlesource.com/aom/+archive/refs/tags/v3.5.0.tar.gz",
             "aom.tar.gz", "aom"],
        "folder_name": "aom_build"
    },
    "libass":{
        "configure_opts": ["--disable-shared", "--enable-static"],
        "dependencies": ["libfontconfig", "libfreetype", "libfribidi", "harfbuzz"],
        "download_opts": ["https://github.com/libass/libass/releases/download/0.16.0/libass-0.16.0.tar.xz",
            "libass-0.16.0.tar.xz"],
        "folder_name": "libass-0.16.0"
    },
    "libbluray":{
        "configure_opts": ["--disable-shared", "--enable-static", "--disable-bdjava-jar", "--without-libxml2"],
        "dependencies": ["libfontconfig", "libfreetype", "libudfread"],
        "download_opts": ["https://code.videolan.org/videolan/libbluray/-/archive/1.3.3/libbluray-1.3.3.tar.gz",
            "libbluray-1.3.3.tar.gz"],
        "folder_name": "libbluray-1.3.3"
    },
    "libdav1d":{
        "configuration": "meson",
        "configure_opts": ["--default-library=static", "-Denable_tools=false", "-Denable_tests=false"],
        "download_opts": ["https://code.videolan.org/videolan/dav1d/-/archive/1.0.0/dav1d-1.0.0.tar.gz", "dav1d-1.0.0.tar.gz"],
        "folder_name": "dav1d_build"
    },
    "libfdk-aac":{
        "configure_opts": ["--disable-shared", "--enable-static"],
        "download_opts": ["https://github.com/mstorsjo/fdk-aac/archive/refs/tags/v2.0.2.tar.gz",
            "fdk-aac-2.0.2.tar.gz"],
        "folder_name": "fdk-aac-2.0.2"
    },
    "libfontconfig":{
        "configure_opts": ["--disable-shared", "--enable-static", "--disable-docs"],
        "dependencies": ["libfreetype"],
        "download_opts": ["https://www.freedesktop.org/software/fontconfig/release/fontconfig-2.14.1.tar.xz",
            "fontconfig-2.14.1.tar.xz"],
        "folder_name": "fontconfig-2.14.1"
    },
    "libfreetype":{
        "configure_opts": ["--disable-shared", "--enable-static", "--with-bzip2=no", "--with-png=no", "--with-harfbuzz=no", "--with-brotli=no", "--with-librsvg=no"],
        "download_opts": ["https://download.savannah.gnu.org/releases/freetype/freetype-2.12.1.tar.xz",
            "freetype-2.12.1.tar.xz"],
        "folder_name": "freetype-2.12.1"
    },
    "libfribidi":{
        "configure_opts": ["--disable-shared", "--enable-static"],
        "download_opts": ["https://github.com/fribidi/fribidi/releases/download/v1.0.12/fribidi-1.0.12.tar.xz",
            "fribidi-1.0.12.tar.xz"],
        "folder_name": "fribidi-1.0.12"
    },
    "libmp3lame":{
        "configure_opts": ["--disable-shared", "--enable-static"],
        "download_opts": ["https://codeload.github.com/openstreamcaster/lame/zip/master",
            "lame-master.zip"],
        "folder_name": "lame-master"
    },
    "libkvazaar":{
        "configure_opts": ["--disable-shared", "--enable-static"],
        "download_opts": ["https://github.com/ultravideo/kvazaar/releases/download/v2.1.0/kvazaar-2.1.0.tar.xz",
            "kvazaar-2.1.0.tar.xz"],
        "folder_name": "kvazaar-2.1.0"
    },
    "libogg":{
        "configure_opts": ["--disable-shared", "--enable-static"],
        "download_opts": ["http://downloads.xiph.org/releases/ogg/libogg-1.3.5.tar.gz",
            "libogg-1.3.5.tar.gz"],
        "folder_name": "libogg-1.3.5"
    },
    "libopencore":{
        "configure_opts": ["--disable-shared", "--enable-static"],
        "download_opts": ["https://downloads.sourceforge.net/project/opencore-amr/opencore-amr/opencore-amr-0.1.6.tar.gz",
            "opencore-amr-0.1.6.tar.gz"],
        "folder_name": "opencore-amr-0.1.6"
    },
    "libopenh264":{
        "configuration": "meson",
        "configure_opts": ["--default-library=static"],
        "download_opts": ["https://github.com/cisco/openh264/archive/refs/tags/v2.3.1.tar.gz",
            "v2.3.1.tar.gz"],
        "folder_name": "openh264_build"
    },
    "libopus":{
        "configure_opts": ["--disable-shared", "--enable-static"],
        "download_opts": ["https://archive.mozilla.org/pub/opus/opus-1.3.1.tar.gz",
            "opus-1.3.1.tar.gz"],
        "folder_name": "opus-1.3.1"
    },
    "libsdl":{
        "configure_opts": ["--disable-shared", "--enable-static"],
        "download_opts": ["https://github.com/libsdl-org/SDL/releases/download/release-2.24.2/SDL2-2.24.2.tar.gz",
            "SDL2-2.24.2.tar.gz"],
        "folder_name": "SDL2-2.24.2"
    },
    "libsoxr":{
        "configuration": "cmake",
        "configure_opts": ["-DBUILD_SHARED_LIBS=off", "."],
        "download_opts": ["https://github.com/chirlu/soxr/archive/refs/tags/0.1.3.tar.gz",
            "0.1.3.tar.gz"],
        "folder_name": "soxr-0.1.3"
    },
    "libsvtav1":{
        "configuration": "cmake",
        "configure_opts": ["-DBUILD_DEC=OFF", "-DBUILD_SHARED_LIBS=OFF"],
        "download_opts": ["https://gitlab.com/AOMediaCodec/SVT-AV1/-/archive/v1.3.0/SVT-AV1-v1.3.0.tar.gz",
            "SVT-AV1-v1.3.0.tar.gz"],
        "folder_name": "SVT-AV1-v1.3.0"
    },
    "libtheora":{
        "configure_opts": ["--disable-shared", "--enable-static", "--disable-oggtest", "--disable-vorbistest", "--disable-examples", "--disable-asm", "--disable-spec"],
        "dependencies": ["libogg","libvorbis"],
        "download_opts": ["http://downloads.xiph.org/releases/theora/libtheora-1.1.1.tar.bz2",
            "libtheora-1.1.1.tar.bz"],
        "folder_name": "libtheora-1.1.1"
    },
    "libtasn1":{
        "configure_opts": ["--disable-shared", "--enable-static", "--disable-doc"],
        "download_opts": ["https://ftp.gnu.org/gnu/libtasn1/libtasn1-4.19.0.tar.gz",
            "libtasn1-4.19.0.tar.gz"],
        "folder_name": "libtasn1-4.19.0"
    },
    "libudfread":{
        "configure_opts": ["--disable-shared", "--enable-static"],
        "download_opts": ["https://code.videolan.org/videolan/libudfread/-/archive/1.1.2/libudfread-1.1.2.tar.gz",
            "libudfread-1.1.2.tar.gz"],
        "folder_name": "libudfread-1.1.2"
    },
    "libunistring":{
        "configure_opts": ["--disable-shared", "--enable-static"],
        "download_opts": ["https://ftp.gnu.org/gnu/libunistring/libunistring-1.1.tar.xz",
            "libunistring-1.1.tar.xz"],
        "folder_name": "libunistring-1.1"
    },
    "libvidstab":{
        "configuration": "cmake",
        "configure_opts": ["-DBUILD_SHARED_LIBS=OFF", "-DUSE_OMP=OFF", "-DENABLE_SHARED=off", "."],
        "download_opts": ["https://github.com/georgmartius/vid.stab/archive/v1.1.0.tar.gz",
            "vidstab-1.1.0.tar.gz"],
        "folder_name": "vid.stab-1.1.0"
    },
    "libvmaf": {
        "configuration": "meson",
        "configure_opts": ["--default-library=static", "libvmaf"],
        "download_opts": ["https://github.com/Netflix/vmaf/archive/refs/tags/v2.3.1.tar.gz",
            "v2.3.1.tar.gz"],
        "folder_name": "vmaf-2.3.1"
    },
    "libvorbis":{
        "configure_opts": ["--disable-shared", "--enable-static", "--disable-oggtest"],
        "dependencies": ["libogg"],
        "download_opts": ["http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.7.tar.gz",
            "libvorbis-1.3.7.tar.gz"],
        "folder_name": "libvorbis-1.3.7"
    },
    "libvpx":{
        "configure_opts": ["--disable-shared", "--disable-unit-tests", "--disable-examples", "--enable-vp9-highbitdepth"],
        "download_opts": ["https://github.com/webmproject/libvpx/archive/refs/tags/v1.12.0.tar.gz",
            "libvpx-1.12.0.tar.gz"],
        "folder_name": "libvpx-1.12.0"
    },
    "libx264":{
        "configure_opts": ["--enable-static", "--enable-pic"],
        "download_opts": ["https://code.videolan.org/videolan/x264/-/archive/stable/x264-stable.tar.gz",
            "x264-stable.tar.gz"],
        "folder_name": "x264-stable"
    },
    "libx265":{
        "configuration": "cmake",
        "configure_opts": ["-DENABLE_SHARED=off", "."],
        "download_opts": ["https://bitbucket.org/multicoreware/x265_git/downloads/x265_3.5.tar.gz",
            "x265_3.5.tar.gz"],
        "folder_name": ["x265_3.5", "source"]
    },
    "libxvid":{
        "configure_opts": ["--disable-shared", "--enable-static"],
        "download_opts": ["https://downloads.xvid.com/downloads/xvidcore-1.3.7.tar.gz",
            "xvidcore-1.3.7.tar.gz"],
        "folder_name": ["xvidcore", "build", "generic"]
    },
    "libzimg":{
        "configure_opts": ["--disable-shared", "--enable-static"],
        "download_opts": ["https://github.com/sekrit-twc/zimg/archive/refs/tags/release-3.0.4.tar.gz",
            "zimg-3.0.4.tar.gz"],
        "folder_name": "zimg-release-3.0.4"
    },
    "nettle":{
        "configure_opts": ["--disable-shared", "--enable-static", "--disable-documentation"],
        "dependencies": ['gmp'],
        "download_opts": ["https://ftp.gnu.org/gnu/nettle/nettle-3.8.1.tar.gz",
            "nettle-3.8.1.tar.gz"],
        "folder_name": "nettle-3.8.1"
    },
    "openssl":{
        "configure_opts": [],
        "download_opts": ["https://www.openssl.org/source/openssl-1.1.1s.tar.gz",
            "openssl-1.1.1s.tar.gz"],
        "folder_name": "openssl-1.1.1s"
    },
    "pkg-config":{
        "configure_opts": ["--silent", "--with-internal-glib"],
        "download_opts": ["http://pkgconfig.freedesktop.org/releases/pkg-config-0.29.2.tar.gz",
            "pkg-config-0.29.2.tar.gz"],
        "folder_name": "pkg-config-0.29.2"
    },
    "nasm":{
        "configure_opts": ["--disable-shared", "--enable-static"],
        "download_opts": ["https://www.nasm.us/pub/nasm/releasebuilds/2.15.05/nasm-2.15.05.tar.xz",
            "nasm.tar.gz"],
        "folder_name": "nasm-2.15.05"
    },
    "yasm":{
        "download_opts": ["http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz",
            "yasm-1.3.0.tar.gz"],
        "folder_name": "yasm-1.3.0"
    },
    "zlib":{
        "configure_opts": ["--static"],
        "download_opts": ["https://www.zlib.net/zlib-1.2.13.tar.xz",
            "zlib-1.2.13.tar.xz"],
        "folder_name": "zlib-1.2.13",
    }
}
SHELL = 'bash'

# Set up constants
DOWNLOAD_RETRY_DELAY = 3
DOWNLOAD_RETRY_ATTEMPTS = 3

# Pseudographics
BOLD_SEPARATOR = "======================================="
ITALIC_SEPARATOR = "---------------------------------------"

def lookahead(iterable):
    it=iter(iterable)
    for value in it:
        try:
            yield value, next(it)
        except StopIteration:
            yield value, False

def print_lines(*strings):
    to_print = ""
    for line, has_more in lookahead(strings):
        to_print = to_print + line + (os.linesep if has_more else "")
    print(to_print)


def print_header(*strings):
    to_print = strings + (ITALIC_SEPARATOR,)
    print_lines(*to_print)


def print_block(*strings):
    to_print = strings + (BOLD_SEPARATOR,)
    print_lines(*to_print)
    print("")


def print_p(*strings):
    to_print = strings
    print_lines(*to_print)
    print("")

# Please note that neat features of Plumbum like FG, BG and TEE are not working on Windows.
# Especially TEE that runs `select` against new processes.
# Therefore, now we have no meaningful debug output whatsoever.
# It's a huge problem, but I know no quick fixes, and Windows is too important now.
# https://github.com/tomerfiliba/plumbum/issues/170
#
# A temporary solution:
# Plumbum provides enough information for a very basic log-driven debugging though.
# For a deep understanding of underlying errors you have to hack this script by yourself to add some reporting.

def fg(command: str, *args, silent: bool=False) -> bool:
    """
    Run command at foreground

    Parameters
    ----------
    command: str
        Command
    *args
        Command additional argument
    silent: bool
        Print foreground result or not

    Returns
    -------
    bool
    """
    try:
        if silent:
            (local[command][args])() #pylint: disable=pointless-statement
        else:
            local[command][args] & FG #pylint: disable=pointless-statement
        return True
    except Exception as e: #pylint: disable=broad-except
        print(f"Failed to execute in foreground\n{e}")
        return False

def add_path(dir_name: str, take_priority: bool=True) -> None:
    """
    Add directory to PATH env

    Parameters
    ----------
    dir_name: str
        Directory name/path
    take_priority: bool (default True)
        If true, the directory will be prioritized

    Returns
    -------
    None
    """
    old_path = local.env["PATH"]
    if take_priority:
        new_path = f"{dir_name}:{old_path}"
    else:
        new_path = f"{old_path}:{dir_name}"
    local.env["PATH"] = new_path

def mkdir(*dir_tree) -> None:
    """
    Create directory

    Parameters
    ----------
    *dir_tree
        Directory hierarcy

    Retuns
    ------
    None
    """
    dir_name = path_join(*dir_tree)
    if not os.path.exists(dir_name):
        Path(dir_name).mkdir(parents=True, exist_ok=True)
        if is_exists(dir_name):
            print(f"Directory {dir_name} created successfully")
            return
        print(f"Directory {dir_name} can't be created")
        return
    print(f"Directory {dir_name} already exists, can't create")

def mkdirs(*dirs) -> None:
    """
    Create multiple directiory

    Parameters
    ----------
    *dirs
        Directory

    Returns
    -------
    None
    """
    for current_dir in dirs:
        mkdir(current_dir)

def rmdir(dir_name: str) -> None:
    """
    Remove directory

    Parameters
    ----------
    dir_name: str
        Directory name that you wanna remove

    Returns
    -------
    None
    """
    if not os.path.exists(dir_name):
        print(f"Directory {dir_name} doesn't exist, no need to remove it")
        return
    rmtree(dir_name, ignore_errors=True)
    if is_exists(dir_name):
        print(f"Directory {dir_name} still exists, can't remove")
        return
    print(f"Directory {dir_name} removed successfully")

def rm(*file_tree) -> None:
    """
    Remove file

    Parameters
    ----------
    *file_tree
        File location hierarcy

    Returns
    -------
    None
    """
    file_name = path_join(*file_tree)
    if not os.path.exists(file_name):
        print(f"File {file_name} doesn't exist, no need to remove it")
        return
    os.remove(file_name)
    if is_exists(file_name):
        print(f"File {file_name} still exists, can't remove")
        return
    print(f"File {file_name} removed successfully")

def command_exists(cmd: str) -> bool:
    """
    Check if commands exist

    Parameters
    ----------
    cmd: str
        Command name

    Returns
    -------
    bool
    """
    try:
        local[cmd] #pylint: disable=pointless-statement
        return True
    except CommandNotFound:
        return False

def require_commands(*commands) -> None:
    """
    Check if required commands exist

    Parameters
    ----------
    *commands
        List of commands

    Returns
    -------
    None
    """
    absent_commands_list = [command for command in commands if not command_exists(command)]
    if absent_commands_list:
        absent = ', '.join(absent_commands_list)
        print(f"Required commands not found: {absent}")
        sys_exit(1)

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
    rmdir(release_dir)
    rmdir(target_dir)
    print("Cleaning finished")

def make(threads: int, *args, **kwargs) -> None:
    """
    Make command

    Parameters
    ----------
    threads: int
        How many threads
    *args
        Will be passed to fg function
    **kwargs
        Will be passed to fg function

    Returns
    -------
    None
    """
    print("Running make...")
    if not fg("make", "-j", threads, *args, **kwargs):
        sys_exit(1)
    print("Make done.")

def install(*args, **kwargs) -> None:
    """
    Make install

    Parameters
    ----------
    *args
        Will be passed to fg function
    **kwargs
        Will be passed to fg function

    Returns
    -------
    None
    """
    print("Installing...")
    if not fg("make", "install", *args,  **kwargs):
        sys_exit(1)
    print("Installation done.")

class Builder:
    """
    Class to build ffmpeg
    """
    def __init__(self,
            os_type,
            target_dir: str="targets",
            release_dir: str="release",
            bin_dir: str="bin",
        ):
        self.__dir_data={
            "target_dir": path_join(CWD(), target_dir),
            "release_dir": path_join(CWD(), release_dir),
            "bin_dir": path_join(CWD(), release_dir, bin_dir),
            "pkg_config_path": path_join(CWD(), release_dir, "lib", "pkgconfig")
        }
        self.__ffmpeg_opts = tuple()

        #Value will filled at build function
        self.__event={
                'pre_dependency': self.__pre_dependency,
                'post_download': self.__post_download,
                'pre_configure': self.__pre_configure,
                'post_configure': self.__post_configure,
                'post_install': self.__post_install,
            }
        self.__is_slavery=False
        self.__old_ldflags=None
        self.__os_type=os_type
        self.__targets=[]

    @property
    def target_dir(self) -> str:
        """
        Returns
        -------
        str
            Return target dir
        """
        return self.__dir_data['target_dir']

    @property
    def release_dir(self) -> str:
        """
        Returns
        -------
        str
            Returnr release dir
        """
        return self.__dir_data['release_dir']

    @property
    def bin_dir(self) -> str:
        """
        Returns
        -------
        str
            Return binary dir
        """
        return self.__dir_data['bin_dir']

    @property
    def pkg_config_path(self) -> str:
        """
        Returns
        -------
        str
            Return pkg config path
        """
        return self.__dir_data['pkg_config_path']

    @property
    def is_windows(self) -> bool:
        """
        Returns
        -------
        bool
        """
        return self.__os_type == 'Windows'

    @property
    def is_linux(self) -> bool:
        """
        Returns
        -------
        bool
        """
        return self.__os_type == 'Linux'

    @property
    def is_mac(self) -> bool:
        """
        Returns
        -------
        bool
        """
        return self.__os_type == 'Darwin'

    def __add_ffmpeg_lib(self, lib: str) -> None:
        """
        Add enabled library to ffmpeg configuration

        Parameters
        ----------
        lib: str
            Library name
        """
        if lib in ('libogg', 'libsdl', "libudfread"):
            return
        if lib == 'libopencore':
            LIBRARIES['ffmpeg']['configure_opts'].extend([
                "--enable-libopencore_amrnb",
                "--enable-libopencore_amrwb"
            ])
            return
        #Cuurrenty an issue in libvmaf also requires FFmpeg to be built with --ld="g++" for a static build to succeed.
        if lib == 'libvmaf':
            LIBRARIES['ffmpeg']['configure_opts'].append("--ld=\"g++\"")
        LIBRARIES['ffmpeg']['configure_opts'].append(f"--enable-{lib}")
        return

    def __configuration_handler(self, threads: int, silent: bool, library: str) -> bool:
        """
        Handle library configuration

        Parameters
        ----------
        threads: int
            Parallel jobs for make command
        silent: bool
            Verbose or not
        library: str
            Library name

        Returns
        -------
        bool
        """
        if library == "ffmpeg-windows-deps-master":
            fg("cp", "-f", "./*", f"{self.release_dir}/bin")
            self.mark_as_built("ffmpeg-msys2-deps")
            return True
        if library == 'libx264' and self.is_linux:
            with local.env(CXXFLAGS="-fPIC"):
                self.configure(*LIBRARIES['libx264'].get("configure_opts", []), silent=silent)
                return False
        if library == 'openssl':
            if not fg("bash",
                "./config",
                *LIBRARIES['openssl'].get("configure_opts", [])):
                sys_exit(1)
            return False
        if library == 'zlib':
            if self.is_windows:
                # Problem 1:
                # Please note that
                # Checking for gcc...
                # Please use win32/Makefile.gcc instead.
                # ** ./configure aborting.
                #
                # Problem 2:
                # Making done.
                # Installing...
                # INCLUDE_PATH, LIBRARY_PATH, and BINARY_PATH must be specified
                # make: *** [win32/Makefile.gcc:128: install] Error 1
                with local.env(INCLUDE_PATH=f"{self.release_dir}/include",
                    LIBRARY_PATH=f"{self.release_dir}/lib",
                    BINARY_PATH=f"{self.release_dir}/bin"):
                    make(threads, "-f", "./win32/Makefile.gcc")
                    install("-f", "./win32/Makefile.gcc")
                    self.mark_as_built('zlib')
                    return True
            self.configure(*LIBRARIES['zlib'].get("configure_opts", []), silent=silent)
            make(threads, silent=silent)
            install(silent=silent)
            self.mark_as_built('zlib')
            return True

        if LIBRARIES[library].get("configuration", "configure") == "meson":
            self.meson(*LIBRARIES[library].get("configure_opts", []), silent=silent)
            fg("ninja", "-j", threads, silent=silent)
            fg("ninja", "install")
            self.mark_as_built(library)
            return True
        if LIBRARIES[library].get("configuration", "configure") == "cmake":
            self.cmake(*LIBRARIES[library].get("configure_opts", []), silent=silent)
            return False
        self.configure(*LIBRARIES[library].get("configure_opts", []), silent=silent)
        return False

    def __pre_dependency(self, lib: str) -> None:
        """
        This function will executed before dependency check

        Parameters
        ----------
        lib: str
            Library name

        Returns
        -------
        None
        """
        if lib == 'harfbuzz':
            if 'libfreetype' in self.__targets:
                LIBRARIES['harfbuzz']['configure_opts'].append("--with-freetype=yes")
                LIBRARIES['harfbuzz']["dependencies"]=['libfreetype']
                return
            LIBRARIES['harbuzz']['configure_opts'].append("--with-freetype=no")

        elif lib == 'libfreetype':
            if 'zlib' in self.__targets:
                LIBRARIES['libfreetype']['configure_opts'].append("--with-zlib=yes")
                LIBRARIES['libfreetype']["dependencies"]=['zlib']
                return
            LIBRARIES['libfreetype']['configure_opts'].append("--with-zlib=no")

    def __post_download(self, lib: str) -> None:
        """
        This function will executed after download finished

        Parameters
        ----------
        lib: str
            Library name

        Returns
        -------
        None
        """
        if lib == "libaom":
            mkdir(self.target_dir, LIBRARIES['libaom']['folder_name'])

        elif lib == 'libopenh264':
            mkdir(self.target_dir, LIBRARIES['libopenh264']['folder_name'])

        elif lib == 'libdav1d':
            mkdir(self.target_dir, LIBRARIES['libdav1d']['folder_name'])

    def __pre_configure(self, lib: str) -> None:
        """
        This function will executed before configure

        Parameters
        ----------
        lib: str
            Library name

        Returns
        -------
        None
        """
        if lib == 'cmake':
            rm("Modules", "FindJava.cmake")
            (local["perl"][ "-p", "-i", "-e", "s/get_filename_component.JNIPATH/#get_filename_component(JNIPATH/g", "Tests/CMakeLists.txt"])()

        elif lib == 'ffmpeg':
            LIBRARIES['ffmpeg']['configure_opts'].extend([
                *self.__ffmpeg_opts,
                # f"--bindir={self.path_fixer(self.release_dir)}/bin"
                # f"--libdir={self.path_fixer(self.release_dir)}/lib",
                f"--pkgconfigdir={self.path_fixer(self.release_dir)}/lib/pkgconfig",
                f"--extra-cflags=-I{self.path_fixer(self.release_dir)}/include",
                f"--extra-ldflags=-L{self.path_fixer(self.release_dir)}/lib -fstack-protector"
            ])
            for ffmpeg_lib in LIBRARIES:
                if ffmpeg_lib.startswith("lib") or ffmpeg_lib in ("openssl", "zlib"):
                    if ffmpeg_lib in self.__targets:
                        self.__add_ffmpeg_lib(ffmpeg_lib)

            if 'gmp' in self.__targets:
                LIBRARIES['ffmpeg']['configure_opts'].append('--enable-gmp')

            if 'libsdl' in self.__targets:
                LIBRARIES['ffmpeg']['configure_opts'].append('--enable-ffplay')

            if not self.__is_slavery and 'gnutls' in self.__targets:
                print("Applying free replacements for non-free components")
                LIBRARIES['ffmpeg']['configure_opts'].append("--enable-gnutls")

            elif self.__is_slavery:
                print_p("You are applying dirty non-free attachments. Are you sure you need this?",
                        "Now you can't distribute this FFmpeg build to anyone, so it's almost useless in real products.",
                        "You can't sell or give away these files")
                LIBRARIES['ffmpeg']['configure_opts'].append("--enable-nonfree")
                    # Non-free unfortunately
                    # Should be replaced with gnutls
                    # http://www.iiwnz.com/compile-ffmpeg-with-rtmps-for-facebook
                    # libfdk_aac is incompatible with the gpl and --enable-nonfree is not specified.
                        # https://trac.ffmpeg.org/wiki/Encode/AAC

            # Unfortunately even creators of MSYS2 can't build it with --enable-pthreads :(
            # https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-ffmpeg/PKGBUILD
            if not self.is_windows:
                LIBRARIES['ffmpeg']['configure_opts'].extend(["--extra-libs=-lpthread", "--enable-pthreads"])

        elif lib == "libaom":
            # TODO: Don't forget about different kinds of cmake (msys/cmake and mingw/cmake)
            LIBRARIES['libaom']['configure_opts'].append(f"{self.target_dir}/aom")

        elif lib == 'libbluray':
            fg("autoreconf", "-fiv")

        elif lib == 'libdav1d':
            LIBRARIES['libdav1d']['configure_opts'].extend([f"--libdir={self.release_dir}/lib", f"{self.target_dir}/dav1d-{re_findall('dav1d-(.+).tar', LIBRARIES['libdav1d']['download_opts'][1])[0]}"])

        elif lib == 'libfdk-aac':
            fg("autoreconf", "-fiv")

        elif lib == 'libopenh264':
            LIBRARIES['libopenh264']['configure_opts'].extend([f"--libdir={self.release_dir}/lib",f"{self.target_dir}/openh264-{re_findall('v(.+).tar', LIBRARIES['libopenh264']['download_opts'][1])[0]}"])

        elif lib == 'libopus':
            # On Windows, there's a huge problem.
            # "Unlike glibc, mingw-w64 does not provide fortified functions at all...
            # "... actually it does now, but its broken as hell :S"
            #
            # MinGW: https://github.com/msys2/MINGW-packages/issues/5803
            # Opus: https://github.com/bincrafters/community/issues/1077
            #
            # Solution:
            # Fortification requires -lssp (or -fstack-protector which adds -lssp implicitly) to work.
            self.__old_ldflags = local.env.get("LDFLAGS")
            if self.is_windows:
                if self.__old_ldflags is not None:
                    local.env["LDFLAGS"] = f"{self.__old_ldflags} -fstack-protector"
                    return
                local.env["LDFLAGS"] = " -fstack-protector"

        elif lib == 'libtheora':
            print("Removing --fforce-adr from configure")
            ((local["sed"]["s/-fforce-addr//g", "configure"]) > "configure.patched") & FG #pylint: disable=pointless-statement
            fg("chmod", "+x", "configure.patched")
            fg("mv", "configure.patched", "configure")
            print("Configure processing done.")
            LIBRARIES['libtheora']['configure_opts'].extend([
                f"--with-ogg-libraries={self.release_dir}/lib",
                f"--with-ogg-includes={self.release_dir}/include/",
                f"--with-vorbis-libraries={self.release_dir}/lib",
                f"--with-vorbis-includes={self.release_dir}/include/"
            ])

        elif lib == 'libudfread':
            fg("autoreconf", "-fiv")

        elif lib == 'libvmaf':
            LIBRARIES['libvmaf']['configure_opts'].append(f"--libdir={self.release_dir}/lib")

        elif lib == 'libvorbis':
            LIBRARIES['libvorbis']['configure_opts'].extend([
                f"--with-ogg-libraries={self.path_fixer(self.release_dir)}/lib",
                f"--with-ogg-includes={self.path_fixer(self.release_dir)}/include"
            ])

        elif lib == "libvpx" and self.is_mac:
            print("Patching libvpx for MacOS")
            ((local["sed"]["s/,--version-script//g", "build/make/Makefile"]) > "build/make/Makefile.patched")()
            ((local["sed"]["s/-Wl,--no-undefined -Wl,-soname/-Wl,-undefined,error -Wl,-install_name/g",
                "build/make/Makefile.patched"]) > "build/make/Makefile")()

        elif lib == 'libzimg':
            fg("autoreconf", "-fiv")

        elif lib == 'openssl':
            LIBRARIES['openssl']['configure_opts'].extend([
                f"--prefix={self.path_fixer(self.release_dir)}",
                f"--openssldir={self.path_fixer(self.release_dir)}",
                f"--with-zlib-include={self.path_fixer(self.release_dir)}/include/",
                f"--with-zlib-lib={self.path_fixer(self.release_dir)}/lib",
                "no-shared",
                "zlib"
            ])

        elif lib == 'pkg-config':
            LIBRARIES['pkg-config']['configure_opts'].append(f"--with-pc-path={self.release_dir}/lib/pkgconfig")

    def __post_configure(self, lib: str) -> None:
        """
        This function will executed after configuring

        Parameters
        ----------
        lib: str
            Library name

        Returns
        -------
        None
        """
        if lib == "libmp3lame":
            # First attempt was to use lame-3.100:
            # http://kent.dl.sourceforge.net/project/lame/lame/3.100/lame-3.100.tar.gz
            # But old version 3.100 breaks Windows compatibility when using libiconv
            # since frontend/parse.c now depends on langinfo.h.
            # https://github.com/bincrafters/community/issues/480
            #
            # We have option to use the latest snapshot from SVN:
            # https://sourceforge.net/p/lame/svn/HEAD/tarball
            # https://sourceforge.net/code-snapshots/svn/l/la/lame/svn/lame-svn-r6449-trunk.zip
            # And get the exact version with: https://sourceforge.net/projects/lame/best_release.json
            #
            # But for now I just imported everything into OpenStreamCaster's space on GitHub:
            # https://codeload.github.com/openstreamcaster/lame/zip/master
            fg("chmod", "+x", "install-sh")

        elif lib == 'libopus':
            # Restore old LDFLAGS after all that dark magic
            if self.is_windows and self.__old_ldflags is not None:
                local.env["LDFLAGS"] = self.__old_ldflags

    def __post_install(self, lib: str):
        """
        This function will executed after installing

        Parameters
        ----------
        lib: str
            Library name

        Returns
        -------
        None
        """
        if lib == 'libx265':
            ((local["sed"][
                "s/-lx265/-lx265 -lstdc++/g",
                f"{self.path_fixer(self.release_dir)}/lib/pkgconfig/x265.pc"]
            ) > f"{self.path_fixer(self.release_dir)}/lib/pkgconfig/x265.pc.tmp")()
            fg("mv", f"{self.path_fixer(self.release_dir)}/lib/pkgconfig/x265.pc.tmp", f"{self.path_fixer(self.release_dir)}/lib/pkgconfig/x265.pc")

        elif lib == 'libxvid':
            dylib_file = path_join(self.target_dir, "lib", "libxvidcore.4.dylib")
            if is_exists(dylib_file):
                rm(dylib_file)

    def __build_library(self,
            library: str,
            threads: int,
            is_dependency=False,
            silent: bool=False) -> None:
        """
        This function will handle the build process

        Parameters
        ----------
        library: str
            Library name
        threads: int
            How many threads
        is_dependency: bool (default False)
            If the library is needed by other library
        silent: bool (default False)
            Verbose or not

        Returns
        -------
        None
        """
        if not self.is_needed(library) and not is_dependency:
            return
        self.__event['pre_dependency'](library)
        if len(LIBRARIES[library].get('dependencies', [])) != 0:
            for dependency in LIBRARIES[library]['dependencies']:
                if not self.is_already_build(dependency):
                    self.__build_library(dependency, threads, is_dependency=True)

        self.download(*LIBRARIES[library]['download_opts'])
        self.__event['post_download'](library)
        with self.target_cwd(*LIBRARIES[library]['folder_name'] if isinstance(LIBRARIES[library]['folder_name'], list) else [LIBRARIES[library]['folder_name']]):
            self.__event['pre_configure'](library)
            if self.__configuration_handler(threads, silent, library):
                return
            self.__event['post_configure'](library)
            make(threads, silent=silent)
            install(silent=silent)
            self.__event['post_install'](library)
            self.mark_as_built(library)

    def build(self,
            targets: list,
            threads: Optional[int]=None,
            is_slavery_mode: bool=False,
            extra_cflags: str="",
            extra_ldflags: str="",
            **kwargs
        ) -> None:
        """
        Function to start building

        Parameters
        ----------
        targets: list
            List of library that we will build
        threads: Optional[int]
            Number of threads
        is_slavery_mode: bool (default False)
            Is slavery mode
        extra_cflags: str (default "")
            Extra CFLAGS
        extra_ldflags: str (default "")
            Extra LDFLAGS

        Returns
        -------
        None
        """
        extra_cflags=f"-I{self.release_dir}/include {extra_cflags}"
        extra_ldflags=f"-L{self.release_dir}/lib {extra_ldflags}"
        self.__targets=targets
        self.__is_slavery=is_slavery_mode
        if threads is None:
            from psutil import cpu_count #pylint: disable=import-outside-toplevel
            threads = cpu_count(logical=False)
            if self.is_mac:
                self.__ffmpeg_opts = ("--enable-videotoolbox",)

        print_header("Building process started")
        mkdirs(self.target_dir, self.release_dir)
        add_path(self.bin_dir)

        with local.env(
            CFLAGS=f"{local.env.get('CFLAGS', '')} {extra_cflags}",
            LDFLAGS=f"{local.env.get('LDFLAGS', '')} {extra_ldflags}",
            PKG_CONFIG_LIBDIR=f"{self.path_fixer(self.release_dir)}/lib/pkgconfig"
            ):
            for library in targets:
                self.__build_library(
                    library,
                    threads,
                    **kwargs
                )

        print_block()
        print_block(f"Finished: {self.path_fixer(self.release_dir)}/bin/ffmpeg",
                    "You can check correctness of this build by running: "
                    f"{self.path_fixer(self.release_dir)}/bin/ffmpeg -version",
                    "Study the protocols list carefully (e.g, look for rtmps): "
                    f"{self.path_fixer(self.release_dir)}/bin/ffmpeg -protocols",
                    "Enable it temporary in the command line by running: "
                    "export PATH={self.path_fixer(self.release_dir)}/bin:$PATH")
        print_block("And finally. Don't trust the build. Anything in the script output may be a lie.",
                    "Always check what you're doing and run test suite.",
                    "If you don't have one, ask for professional help.")

    def configure(self, *opts, **kwargs) -> None:
        """
        Run configure

        Parameters
        ----------
        *args
            Will passed to configure
        **kwargs
            Will passed to fg function

        Returns
        -------
        None
        """
        configure_options = ("./configure", f"--prefix={self.release_dir}",) + opts
        if self.is_windows:
            configure_options = ("bash",) + configure_options
        fg("chmod", "+x", "./configure")
        print(f"Configure with flags: {configure_options}")
        if not fg(*configure_options, **kwargs):
            sys_exit(1)
        print("Configuring done.")

    def cmake(self, *args, **kwargs) -> None:
        """
        Run CMake

        Parameters
        ----------
        *args
            Will passed to CMake
        **kwargs
            Will passed to fg function

        Returns
        -------
        None
        """
        print("Making with CMake...")
        # MSYS2 with MinGW toolchain
        if self.is_windows:
            args = ("-G", "MSYS Makefiles",) + args

        # For POSIX filenames, use 'msys/cmake'.
        # For Windows paths,  mingw64/mingw-w64-x86_64-cmake'
        # Our self-build bundled version of cmake obviously is build with mingw, so we have to use Windows paths here
        # Failing to do so produces incorrect post-installation code in the cmake_install.cmake:
        # ```
        #    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES
        #    "C:/temp/ffmpeg-builder/targets/x265_3.2.1/source/x265.pc")
        # ```
        # Which is triggered by something like this in CMakeLists.txt:
        # ```
        #    configure_file("x265.pc.in" "x265.pc" @ONLY)
        #    install(FILES       "${CMAKE_CURRENT_BINARY_DIR}/x265.pc"
        #    DESTINATION "${LIB_INSTALL_DIR}/pkgconfig")
        #
        # Don't forget that you can search on Windows without grep -r, using
        # something like " dir -Recurse | Select-String -pattern 'x265.pc'" in Power Shell to find errors like this.
        #
        # Discussion: https://cmake.org/pipermail/cmake/2018-February/067058.html
        # Conversions between paths:
        # https://stackoverflow.com/questions/41492504/how-to-get-native-windows-path-inside-msys-python
        # TODO: implement command line option to switch between versions of CMake, protect with cpp(RELEASE_DIR)

        if not fg("cmake", "-DCMAKE_BUILD_TYPE=Release", f"-DCMAKE_INSTALL_PREFIX:PATH={self.release_dir}", *args, **kwargs):
            sys_exit(1)
        print("Making with CMake done.")

    def download(self, url: str, dest_name: str, alternative_dir: Optional[str]=None):
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
            download_path = path_join(download_path, alternative_dir)
            mkdir(download_path)

        base_path = path_join(download_path, dest_name)
        if is_exists(base_path):
            print(f"Used from local cache: {url}")
            return

        print(f"Downloading {url}")
        successful_download = False
        for _ in range(DOWNLOAD_RETRY_ATTEMPTS):
            if fg("curl", "-L", "--silent", "-o", base_path, url) is True:
                successful_download = True
                break
            print(f"Downloading failed: {url}. Retrying in {DOWNLOAD_RETRY_DELAY} seconds")
            sleep(DOWNLOAD_RETRY_DELAY)

        if not successful_download:
            print(f"Failed to download multiple times: {url}")
            sys_exit(1)
        print(f"Successfuly downloaded: {url}")

        if ".tar" in dest_name:
            if fg("tar", "-xvf", self.path_fixer(base_path), "-C", self.path_fixer(download_path), silent=True):
                return
            print(f"Failed to extract {dest_name}")
            sys_exit(1)
        elif ".zip" in dest_name:
            with ZipFile(base_path) as myzip:
                myzip.extractall(download_path)
            return
        raise Exception

    def is_already_build(self, library: str) -> bool:
        """
        Check if library already build

        Parameters
        ----------
        library: str
            The library name

        Returns
        -------
        bool
        """
        return is_exists(path_join(self.target_dir, f"{library}.ok"))

    def is_needed(self, library: str) -> bool:
        """
        Check if library need to build or not

        Parameters
        ----------
        library: str
            The library name

        Returns
        -------
        bool
        """
        if library not in self.__targets:
            return False
        if library == "ffmpeg-msys2-deps" and not self.is_windows:
            return False

        print(f"\nBuilding target: {library}\n{ITALIC_SEPARATOR}")
        if self.is_already_build(library):
            print_block("Cached version found")
            return False
        print("No cache, needs building")
        return True

    def mark_as_built(self, library: str) -> None:
        """
        Mark if the library has been build

        Parameters
        ----------
        library: str
            The library name

        Returns
        -------
        None
        """
        filename = path_join(self.target_dir, f"{library}.ok")
        print_block(f"Creating a lock file: {filename}")
        with open(filename, "w", encoding="utf-8") as _:
            pass

    def meson(self, *args, **kwargs) -> None:
        """
        Run meson

        Parameters
        ----------
        *args
            Will passed to meson
        **kwargs
            Will passed to fg function

        Returns
        -------
        None
        """
        meson_flags=("meson", "setup", f"--prefix={self.release_dir}",) + args
        print(f"Configuring with meson\nFlags: {meson_flags}")
        if not fg(*meson_flags, **kwargs):
            sys_exit(1)
        print("Configure with meson done...")

    def path_fixer(self, src: str) -> str:
        """
        Fix windows path

        Parameters
        ----------
        src: str
            Path

        Returns
        -------
        str
            Fixed path

        Raises
        ------
        NotImplementedError
            Raised if continuing without properly parsed path

        Information
        -----------
        The following code is the poor's man implementation of this:
        https://stackoverflow.com/questions/41492504/how-to-get-native-windows-path-inside-msys-python
        It's working, but maybe we should consider to switch to the full version
        """
        if not self.is_windows:
            return src

        # Handle Windows (native path)
        path_search = re.search('([a-zA-Z]):/(.*)', src, re.IGNORECASE)
        if path_search:
            drive = path_search.group(1).lower()
            path = path_search.group(2)
            result = f"/{drive}/{path}"
            return result
        # Handle Windows (native path with backward slashes)
        # Actually we can skip this, but it's useful for validation
        path_search = re.search('([a-zA-Z]):\\\(.*)', src, re.IGNORECASE)
        if path_search:
            drive = path_search.group(1).lower()
            path = path_search.group(2).replace('\\', '/')
            result = f"/{drive}/{path}"
            return result
        # Handle Windows (MSYS2, Git Bash, Cygwin, etc)
        simulated_path_search = re.search('/([a-zA-Z])/(.*)', src, re.IGNORECASE)
        if simulated_path_search:
            drive = simulated_path_search.group(1).lower()
            path = simulated_path_search.group(2)
            result = f"/{drive}/{path}"
            return result
        # No sense in continuing without properly parsed path
        raise NotImplementedError

    def target_cwd(self, *dirs):
        """
        Change current working directiory

        Parameters
        ----------
        *dirs
            List of directories
        """
        result_dir=self.target_dir
        for curr_dir in dirs:
            result_dir = path_join(result_dir, curr_dir)
        return local.cwd(result_dir)

def main() -> None:
    """
    Program Entry Point

    Returns
    -------
    None
    """
    parser = ArgumentParser(description='Build a special edition of FFMPEG.')
    parser.add_argument('-j', '--jobs', metavar='int', action="store", dest="jobs", type=int, help='Number of parallel jobs', default=None)
    parser.add_argument('-b', '--build', action="store_true", dest="build_mode", help='Run build')
    parser.add_argument('--clean', action="store_true", dest="clean_mode", help='Clean solution')
    parser.add_argument('-q', '--silent', action="store_true", dest="silent_mode", help='Disable build debug')
    parser.add_argument('--targets', action="store", dest="targets",
                    help='comma-separated targets for building (empty = build all)')
    parser.add_argument('--exclude-targets', action="store", dest="exclude_targets", help='Don\'t build these')
    parser.add_argument('--extra-cflags', dest="extra_cflags", help='Build extra CFLAGS')
    parser.add_argument('--extra-ldflags', dest="extra_ldflags", help='Build extra LDFLAGS')
    parser.add_argument('--target-dir', default="targets", help="Target directory")
    parser.add_argument('--release-dir', default="release", help="Release directory")
    parser.add_argument('--use-nonfree-libs', dest="slavery_mode", action='store_true', help="Use non-free libraries", default=False)
    parser.add_argument('--use-system-build-tools', dest="default_tools", action='store_true', help="Use cmake, nasm, yasm, pkg-config that installed on system", default=False)
    parser.add_argument('--disable-ffplay', dest="disable_ffplay", action='store_true', help="Disable building ffplay", default=False)
    args = parser.parse_args()

    targets=['cmake', 'gmp', 'gnutls', 'libaom', 'libass', 'libbluray', 'libdav1d', 'libfdk-aac', 'libfontconfig', 'libfreetype',
             'libfribidi', 'libkvazaar', 'libmp3lame', 'libogg', 'libopus', 'libopencore', 'libopenh264', 'libsdl', 'libsoxr',
             'libsvtav1', 'libtheora', 'libvidstab', 'libvmaf', 'libvorbis', 'libvpx', 'libx264', 'libx265', 'libxvid',
             'libzimg', 'nasm', 'openssl', 'pkg-config', 'yasm', 'zlib', 'ffmpeg-msys2-deps', 'ffmpeg'
            ]
    #Check if user specify specific targets
    targets = [_ for _ in args.targets.split(",") if _ in targets] if args.targets is not None else targets
    #Check if user exclude some targets
    targets = [x for x in targets if x not in args.exclude_targets.split(",") ] if args.exclude_targets is not None else targets
    #Remove cmake, yasm, nasm, and pkg-config from targets if user dont wanna compile it
    targets = [x for x in targets if x not in ('cmake', 'pkg-config', 'nasm', 'yasm')] if args.default_tools else targets
    #Remove libfdk-aac and openssl if not in slavery mode
    targets = [x for x in targets if x not in ('libfdk-aac', 'openssl')] if not args.slavery_mode else targets
    if 'libsdl' in targets and args.disable_ffplay:
        targets.remove('libsdl')
    if not bool(command_exists("meson") and command_exists("ninja")) and any(_ in targets for _ in ("libopenh264", "libdav1d")):
        print("Building libdav1d and libopenh264 now disabled. Meson and ninja weren\'t installed.\nInstall them with `pip install meson ninja`")
        for _ in ('libdav1d', 'libopenh264'):
            try:
                targets.remove(_)
            except ValueError:
                pass

    print_block("Hello, slave, how are you?" if args.slavery_mode else "Building FFmpeg, free as in freedom!")
    print_header("Processing targets:")
    print_block(str(targets))

    if args.build_mode:
        require_commands("autoconf", "libtoolize", "make", "curl", "tar", 'gperf',*['cmake', 'nasm', 'yasm', 'pkg-config'] if args.default_tools else [])
        os_type=system()
        kwargs={}
        if args.jobs is not None:
            kwargs={"threads": args.jobs}
        Builder(os_type, target_dir=args.target_dir, release_dir=args.release_dir).build(
            targets,
            is_slavery_mode=args.slavery_mode,
            silent=args.silent_mode,
            **kwargs
        )

    if args.clean_mode:
        clean_all(args.target_dir, args.release_dir)

    print("OpenStreamCaster's FFmpeg-builder finished its work. And you?\nSee help for more information")

if __name__ == '__main__':
    import re
    import os
    from time import sleep
    from pathlib import Path
    from zipfile import ZipFile
    from argparse import ArgumentParser
    from os import getcwd as CWD
    from os.path import exists as is_exists, join as path_join
    from platform import system
    from shutil import rmtree
    from re import findall as re_findall
    from sys import exit as sys_exit

    try:
        from plumbum import local, FG, CommandNotFound
    except ModuleNotFoundError:
        print("Install plumbum module first")
        sys_exit(1)

    main()
