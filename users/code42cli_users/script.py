import click
from code42cli.extensions import script, sdk_options


@click.command()
@click.option("--guid", required=True)
@sdk_options()
def get_device_user(state, guid):
    settings = state.sdk.devices.get_settings(guid)
    print(settings.user_id)
    
    
if __name__ == "__main__":
    script.add_command(get_device_user)
    script()