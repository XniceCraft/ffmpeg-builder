# pylint: disable = C0114
from options import Options
import file_utils


def pre_configure(ctx, options: Options):
    """
    Pre configuration build patch
    """
    if "openssl" in options.targets:
        ctx.add_configuration_params("-DOPENSSL_USE_STATIC_LIBS=on")
        return
    if "gnutls" in options.targets:
        ctx.add_configuration_params("-DUSE_ENCLIB=gnutls")
        return
    ctx.add_configuration_params("-DENABLE_ENCRYPTION=off")


def pre_dependency(ctx, options: Options):
    """
    Pre dependency build patch
    """
    if "gnutls" in options.targets:
        ctx.add_dependencies("gnutls")
        return
    if "openssl" in options.targets:
        ctx.add_dependencies("openssl")
        return


def post_install(options: Options):
    """
    Post configuration build patch

    Parameters
    ----------
    options : Options
        Build options
    """
    # Fix gcc_s not found
    file_utils.replace(f"{options.release_dir}/lib/pkgconfig/srt.pc", "-lgcc_s", "")
