# pylint: disable = E0402
import re
from options import Options


def pre_configure(ctx, options: Options):
    """
    Pre configuration build patch
    """
    ctx.add_configuration_params(
        f"--libdir={options.release_dir}/lib",
        f"{options.target_dir}/openh264-{re.findall('libopenh264-(.+).tar', ctx.download_params[1])[0]}",
    )
