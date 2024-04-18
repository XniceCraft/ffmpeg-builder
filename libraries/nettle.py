# pylint: disable = C0114
from options import Options
import file_utils


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
        f"{options.release_dir}/lib/pkgconfig/x265.pc",
        "Libs: -L${libdir} -lnettle",
        "Libs: -L${libdir} -lnettle -lgmp",
    )
