from options import Options


def pre_configure(ctx, options: Options):
    """
    Pre configuration build patch
    """
    ctx.add_configuration_params(f"{options.target_dir}/aom")
