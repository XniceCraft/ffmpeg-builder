# pylint: disable = E0402, C0114
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
        f"{options.release_dir}/lib/pkgconfig/gnutls.pc",
        "Libs: -L${libdir} -lgnutls",
        "Libs: -L${libdir} -lgnutls -ltasn1 -lgmp -lunistring -lnettle -lhogweed",
    )
