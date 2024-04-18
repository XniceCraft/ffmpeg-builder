# pylint: disable = C0114
from build_utils import run_fg


def post_configure():
    """
    Post configuration build patch
    """
    run_fg("chmod", "+x", "install-sh")
