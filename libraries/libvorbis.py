# pylint: disable = C0114
from options import Options


def pre_configure(ctx, options: Options):
    """
    Pre configuration build patch
    """
    ctx.add_configuration_params(
        f"--with-ogg-libraries={options.release_dir}/lib",
        f"--with-ogg-includes={options.release_dir}/include",
    )
