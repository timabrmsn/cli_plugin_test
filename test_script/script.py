from code42cli.extensions import sdk_options, script

import click
import pandas as pd
from py42.sdk.queries.fileevents.file_event_query import FileEventQuery
from py42.sdk.queries.fileevents.filters import *


@click.command(help="List a user's devices and recent file events!")
@click.argument("username")
@sdk_options
def my_command(state, username):
    # get user devices
    user = state.sdk.users.get_by_username(username)
    devices = state.sdk.devices.get_all(user_uid=user["users"][0]["userUid"])
    devices_df = pd.json_normalize(next(devices)["computers"])[
        ["name", "active", "guid", "alertStates"]
    ]

    # get recent file events
    query = FileEventQuery.all(
        DeviceUsername.eq(username),
        EventTimestamp.within_the_last(EventTimestamp.THREE_DAYS),
    )
    search_results = state.sdk.securitydata.search_file_events(query)
    events_df = pd.json_normalize(search_results["fileEvents"])[
        ["eventType", "eventTimestamp", "fileName", "fileSize", "fileCategory"]
    ]

    # print results
    click.echo_via_pager(
        "Devices:\n{}\n\nEvents:\n{}".format(
            devices_df.to_string(index=False), events_df.to_string(index=False)
        )
    )


if __name__ == "__main__":
    script.add_command(my_command)
    script()
