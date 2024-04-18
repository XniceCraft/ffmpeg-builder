from options import Options
from build_utils import run_fg


def pre_configure(options: Options):
    """
    Pre configuration build patch
    """
    run_fg("autoreconf", "-fiv", silent=options.silent)
