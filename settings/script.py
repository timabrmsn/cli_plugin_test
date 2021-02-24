import click
from code42cli.extensions import sdk_options


@click.command()
@sdk_options()
def my_command(state):
    print(state.sdk.users.get_current()["username"])


if __name__ == "__main__":
    my_command()