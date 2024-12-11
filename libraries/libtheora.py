# pylint: disable = C0114
from options import Options
from build_utils import run_fg
import file_utils


def pre_configure(ctx, options: Options):
    """
    Pre configuration build patch
    """
    file_utils.replace("configure", "-fforce-addr", "")
    run_fg("chmod", "+x", "configure")
    ctx.add_configuration_params(
        f"--with-ogg-libraries={options.release_dir}/lib",
        f"--with-ogg-includes={options.release_dir}/include/",
        f"--with-vorbis-libraries={options.release_dir}/lib",
        f"--with-vorbis-includes={options.release_dir}/include/",
    )
