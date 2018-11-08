# -- FILE: features/environment.py

    def before_all(context):
        context.app = context.config.userdata["app"]
        context.base_url = context.config.userdata["base_url"]
        context.env = context.config.userdata["env"]
        context.nbx_integration = context.config.userdata["nbx_integration"]
        context.payment_endpoint = context.config.userdata["payment_endpoint"]
        context.resource_dir = context.config.userdata["resources"]
        if context.config.userdata["jump_box"] is not None:
            context.jump_box = context.config.userdata["jump_box"]

    def before_scenario(context):
        context.transaction = {}

    def after_scenario(context):
        del context.transaction
