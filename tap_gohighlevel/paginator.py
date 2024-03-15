"""Pagination support for the GoHighLevel tap."""
from __future__ import annotations

import typing as t

from singer_sdk.pagination import BaseHATEOASPaginator

if t.TYPE_CHECKING:
    from requests import Response

class GoHighLevelPaginator(BaseHATEOASPaginator):
    """GoHighLevel paginator."""
    def get_next_url(self, response: Response) -> str | None:
        """Return the next page URL or None if no more pages.

        Args:
            response: The last API response.
        """
        # TOOD: validate this
        return response.json().get("meta").get("nextPageUrl")
