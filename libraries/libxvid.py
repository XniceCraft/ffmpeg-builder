# pylint: disable = E0402, C0114
from options import Options
import file_utils


def post_configure(options: Options):
    """
    Post configuration build patch

    Parameters
    ----------
    options : Options
        Build options
    """
    file = f"{options.target_dir}/xvidcore/build/generic/Makefile"
    start = file_utils.find_string(file, "ifeq ($(SHARED_EXTENSION),dll)")
    end = (
        file_utils.find_string(
            file, "$(LN_S) $(SHARED_LIB) $(DESTDIR)$(libdir)/$(SO_LINK)"
        )
        + 1
    )
    file_utils.delete_lines(file, start, end)


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
