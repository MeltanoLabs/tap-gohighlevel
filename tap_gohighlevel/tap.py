"""GoHighLevel tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_gohighlevel import streams


class TapGoHighLevel(Tap):
    """GoHighLevel tap class."""

    name = "tap-gohighlevel"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "client_id",
            th.StringType,
            required=True,
            description="Client ID for the API service",
        ),
        th.Property(
            "client_secret",
            th.StringType,
            required=True,
            description="Client Secret for the API service",
        ),
        th.Property(
            "refresh_token",
            th.StringType,
            required=True,
            description="Refresh token for the API service",
        ),
        th.Property(
            "location_id",
            th.StringType,
            required=True,
            description="The Location Id to request data",
            examples=["ve9EPM428h8vShlRW1KT"]
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.GoHighLevelStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.GroupsStream(self),
            streams.UsersStream(self),
        ]


if __name__ == "__main__":
    TapGoHighLevel.cli()
