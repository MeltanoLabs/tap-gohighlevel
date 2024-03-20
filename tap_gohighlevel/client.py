"""REST client handling, including GoHighLevelStream base class."""

from __future__ import annotations

from functools import cached_property
from typing import Any, Callable
from urllib.parse import parse_qsl

import requests
from singer_sdk.pagination import BaseAPIPaginator  # noqa: TCH002
from singer_sdk.streams import RESTStream

from tap_gohighlevel.auth import GoHighLevelAuthenticator
from tap_gohighlevel.paginator import GoHighLevelPaginator

_Auth = Callable[[requests.PreparedRequest], requests.PreparedRequest]

API_VERSION = "2021-07-28"


class GoHighLevelStream(RESTStream):
    """GoHighLevel stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return "https://services.leadconnectorhq.com/"

    records_jsonpath = "$[*]"  # Or override `parse_response`.

    @cached_property
    def authenticator(self) -> _Auth:
        """Return a new authenticator object.

        Returns:
            An authenticator instance.
        """
        return GoHighLevelAuthenticator.create_for_stream(self)

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        return {
            "Version": API_VERSION,
            "Accept": "application/json",
        }

    def get_new_paginator(self) -> BaseAPIPaginator:
        """Create a new pagination helper instance.

        If the source API can make use of the `next_page_token_jsonpath`
        attribute, or it contains a `X-Next-Page` header in the response
        then you can remove this method.

        If you need custom pagination that uses page numbers, "next" links, or
        other approaches, please read the guide: https://sdk.meltano.com/en/v0.25.0/guides/pagination-classes.html.

        Returns:
            A pagination helper instance.
        """
        return GoHighLevelPaginator()

    def get_url_params(
        self,
        context: dict | None,  # noqa: ARG002
        next_page_token: Any | None,  # noqa: ANN401
    ) -> dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        params: dict = {
            "limit": 100,
            "locationId": self.config.get("location_id"),
        }
        if next_page_token:
            params.update(parse_qsl(next_page_token.query))
        elif self.replication_key and self.get_starting_replication_key_value(context):
            params["startAfter"] = self.get_starting_replication_key_value(context)
        return params
