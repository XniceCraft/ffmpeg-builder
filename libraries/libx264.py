# pylint: disable = C0114
import platform
from plumbum import local
from build_utils import configure, make, make_install
from options import Options


def has_own_configuration() -> bool:
    """
    Returns
    -------
    bool
    """
    return platform.system() == "Linux"


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
    with local.env(CXXFLAGS="-fPIC"):
        configure(options.release_dir, *ctx.configure_params, silent=options.silent)
        make(options.threads, silent=options.silent)
        make_install(silent=options.silent)
