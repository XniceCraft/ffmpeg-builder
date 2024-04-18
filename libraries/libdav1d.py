import re
from options import Options


def pre_configure(ctx, options: Options):
    """
    Pre configuration build patch
    """
    ctx.add_configuration_params(
        f"--libdir={options.release_dir}/lib",
        f"{options.target_dir}/dav1d-{re.findall('dav1d-(.+).tar', ctx.download_params[1])[0]}",
    )
