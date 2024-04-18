# pylint: disable = C0114
import sys
from options import Options
from build_utils import run_fg, make
import file_utils


def custom_configure(ctx, options: Options):
    """
    Custom configuration

    Parameters
    ----------
    ctx
        Library class
    options : Options
        Build options
    """
    if not run_fg("bash", "./config", *ctx.configure_params):
        sys.exit(1)
    make(options.threads)
    run_fg("make", "install_sw", f"-j{options.threads}")


def pre_configure(ctx, options: Options):
    """
    Pre configuration build patch
    """
    ctx.add_configuration_params(
        f"--prefix={options.release_dir}",
        f"--openssldir={options.release_dir}",
        f"--with-zlib-include={options.release_dir}/include/",
        f"--with-zlib-lib={options.release_dir}/lib",
        "no-shared",
        "zlib",
    )


def post_install(options: Options):
    """
    Post configuration build patch

    Parameters
    ----------
    options : Options
        Build options
    """
    # Fix static linking issue
    file_utils.replace(
        f"{options.release_dir}/lib/pkgconfig/libcrypto.pc",
        "Libs: -L${libdir} -lcrypto",
        "Libs: -L${libdir} -lcrypto -lz -ldl",
    )
