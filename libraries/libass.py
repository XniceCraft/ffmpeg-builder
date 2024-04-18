# pylint: disable = C0114, line-too-long
from plumbum import local
from build_utils import configure, make, make_install
from options import Options


def custom_configure(ctx, options: Options):
    """
    Custom configuration

    Parameters
    ----------
    options : Options
        Build options
    """
    with local.env(
        CFLAGS=f"{local.env.get('CFLAGS', '')} -I{options.release_dir}/include/harfbuzz"
    ):
        configure(options.release_dir, *ctx.configure_params, silent=options.silent)
        make(options.threads, silent=options.silent)
        make_install(silent=options.silent)
