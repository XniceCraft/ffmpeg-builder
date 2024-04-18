import platform
from options import Options


def add_library(ctx, lib_name: str) -> None:
    """
    Add enabled library to ffmpeg configuration

    Parameters
    ----------
    ctx: Library
        Library class
    lib_name: str
        Library name
    """
    if lib_name in (
        "libogg",
        "libsdl",
        "libudfread",
        "cmake",
        "nasm",
        "pkg-config",
        "ffmpeg",
        "yasm",
        "ffmpeg-msys2-deps",
    ):
        return
    if lib_name == "libopencore":
        ctx.add_configuration_params(
            "--enable-libopencore_amrnb", "--enable-libopencore_amrwb"
        )
        return
    if lib_name == "libvmaf":
        ctx.add_configuration_params("--ld=g++")
    ctx.add_configuration_params(f"--enable-{lib_name}")


def pre_configure(ctx, options: Options):
    """
    Pre configure patch

    Parameters
    ----------
    ctx: Library
        Library class
    options: Options
        Build data
    """
    extra_cflags = " -static -static-libstdc++ -static-libgcc " if options.static_ffmpeg else ""
    extra_ldflags = " -static -static-libstdc++ -static-libgcc " if options.static_ffmpeg else ""
    ctx.add_configuration_params(
        f"--pkgconfigdir={options.release_dir}/lib/pkgconfig",
        f"--extra-cflags=-I{options.release_dir}/include {extra_cflags}",
        f"--extra-ldflags=-L{options.release_dir}/lib -fstack-protector {extra_ldflags}",
    )
    if options.static_ffmpeg:
        ctx.add_configuration_params(
            "--extra-cxxflags=-static -static-libstdc++ -static-libgcc ",
            "--extra-libs=-ldl -lrt -lpthread",
        )
    for library in options.targets:
        add_library(ctx, library)
    if "libsdl" in options.targets:
        ctx.add_configuration_params("--enable-ffplay")
    if options.nonfree_build:
        ctx.add_configuration_params("--enable-nonfree")
    if platform.system() != "Windows":
        ctx.add_configuration_params("--extra-libs=-lpthread", "--enable-pthreads")
    if "libsoxr" in options.targets:
        ctx.add_configuration_params("--extra-libs=-lgomp")
