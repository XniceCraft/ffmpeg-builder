# pylint: disable = C0114
from options import Options


def pre_dependency(ctx, options: Options):
    """
    Pre dependency build patch
    """
    if "libfreetype" in options.targets:
        ctx.add_configuration_params("-DHB_HAVE_FREETYPE=on")
        ctx.add_dependencies("libfreetype")
        return
    ctx.add_configuration_params("-DHB_HAVE_FREETYPE=off")

def pre_configure(ctx, options: Options):
    """
    Pre configuration build patch
    """
    ctx.add_configuration_params(f"{options.target_dir}/harfbuzz-10.1.0")
