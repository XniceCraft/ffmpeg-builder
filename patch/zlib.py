# pylint: disable = C0114
import platform
from plumbum import local
from build_utils import make, make_install
from options import Options


def has_own_configuration() -> bool:
    """
    Returns
    -------
    bool
    """
    return platform.system() == "Windows"


def custom_configure(options: Options):
    """
    Custom configuration

    Parameters
    ----------
    options : Options
        Build options
    """
    with local.env(
        INCLUDE_PATH=f"{options.release_dir}/include",
        LIBRARY_PATH=f"{options.release_dir}/lib",
        BINARY_PATH=f"{options.release_dir}/bin",
    ):
        make(options.threads, "-f", "./win32/Makefile.gcc", silent=options.silent)
        make_install("-f", "./win32/Makefile.gcc", silent=options.silent)
