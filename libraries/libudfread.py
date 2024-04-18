from build_utils import run_fg


def pre_configure():
    """
    Pre configuration build patch
    """
    run_fg("autoreconf", "-fiv")
