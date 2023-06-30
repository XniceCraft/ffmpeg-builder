# pylint: disable = C0114
from options import Options
from build_utils import make_install


def custom_configure(options: Options):
    """
    Custom configuration

    Parameters
    ----------
    options : Options
        Build options
    """
    make_install(f"PREFIX={options.release_dir}", silent=options.silent)
