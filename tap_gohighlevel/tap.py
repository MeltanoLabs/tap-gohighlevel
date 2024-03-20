"""GoHighLevel tap class."""

from __future__ import annotations

from pathlib import Path, PurePath

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers
from singer_sdk.helpers._util import read_json_file

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
            examples=["ve9EPM428h8vShlRW1KT"],
        ),
    ).to_dict()

    def __init__(self, *args, **kwargs):
        config = kwargs.get("config")
        if isinstance(config, (str, PurePath)):
            self._write_back_config_path = Path(config)
        elif isinstance(config, list):
            if len(config) > 1:
                msg = "Multiple config files not supported due to OAuth refresh tokens write back."
                raise Exception(msg)
            self._write_back_config_path = Path(config[0])
        else:
            msg = "Config file must be provided, OAuth refresh tokens need to be written back."
            raise Exception(msg)
        super().__init__(*args, **kwargs)

    def discover_streams(self) -> list[streams.GoHighLevelStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.ContactsStream(self),
        ]


if __name__ == "__main__":
    TapGoHighLevel.cli()
