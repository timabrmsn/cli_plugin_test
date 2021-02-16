import click
from code42cli.extensions import script, sdk_options
from pprint import pprint


@click.command()
@click.option("--guid", required=True)
@sdk_options()
def get_device_settings(state, guid):
    settings_response = state.sdk.devices.get_settings(guid)
    pprint(settings_response.data)


if __name__ == "__main__":
    script.add_command(get_device_settings)
    script()