# pylint: disable = C0114
from options import Options
from build_utils import run_fg


def custom_configure(options: Options):
    """
    Custom configuration

    Parameters
    ----------
    options : Options
        Build options
    """
    run_fg("cp", "-f", "./*", f"{options.release_dir}/bin")
