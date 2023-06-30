# pylint: disable = C0114
from options import Options


def pre_dependency(ctx, options: Options):
    """
    Pre dependency build patch
    """
    if "libfreetype" in options.targets:
        ctx.add_configuration_params("--with-freetype=yes")
        ctx.add_dependencies("libfreetype")
        return
    ctx.add_configuration_params("--with-freetype=no")
