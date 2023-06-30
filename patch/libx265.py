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
    file_utils.replace(
        f"{options.release_dir}/lib/pkgconfig/x265.pc", "-lx265", "-lx265 -lstdc++"
    )
    # Fix gcc_s not found
    file_utils.replace(f"{options.release_dir}/lib/pkgconfig/x265.pc", "-lgcc_s", "")
