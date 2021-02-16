import click
from code42cli.extensions import script, sdk_options


@click.command()
@click.argument("guid")
@sdk_options()
def get_device_user(state, guid):
    settings_response = state.sdk.devices.get_settings(guid)
    print(settings_response.user_id)
    
    
if __name__ == "__main__":
    script.add_command(get_device_user)
    script()