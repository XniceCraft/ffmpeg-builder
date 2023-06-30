# pylint: disable = C0114
from options import Options


def pre_dependency(ctx, options: Options):
    """
    Pre dependency build patch
    """
    if "zlib" in options.targets:
        ctx.add_configuration_params("--with-zlib=yes")
        ctx.add_dependencies("zlib")
        return
    ctx.add_configuration_params("--with-zlib=no")
