"""GoHighLevel Authentication."""

from __future__ import annotations

import requests
from singer_sdk.authenticators import OAuthAuthenticator, SingletonMeta
from singer_sdk.helpers._util import utc_now


# The SingletonMeta metaclass makes your streams reuse the same authenticator instance.
# If this behaviour interferes with your use-case, you can remove the metaclass.
class GoHighLevelAuthenticator(OAuthAuthenticator, metaclass=SingletonMeta):
    """Authenticator class for GoHighLevel."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.refresh_token = str(self.config["refresh_token"])

    @property
    def oauth_request_body(self) -> dict:
        """Define the OAuth request body for the AutomaticTestTap API.

        Returns:
            A dict with the request body
        """
        return {
            "client_id": self.config["client_id"],
            "client_secret": self.config["client_secret"],
            "grant_type": "refresh_token",
            "refresh_token": str(self.config["refresh_token"]),
            "user_type": "Location",
        }

    @classmethod
    def create_for_stream(cls, stream) -> GoHighLevelAuthenticator:  # noqa: ANN001
        """Instantiate an authenticator for a specific Singer stream.

        Args:
            stream: The Singer stream instance.

        Returns:
            A new authenticator.
        """
        return cls(
            stream=stream,
            auth_endpoint="https://services.leadconnectorhq.com/oauth/token",
            oauth_headers={
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            default_expiration=86400 # 24 hours
        )

    def update_access_token(self) -> None:
        """Update `access_token` along with: `last_refreshed` and `expires_in`.

        Raises:
            RuntimeError: When OAuth login fails.
        """
        request_time = utc_now()
        auth_request_payload = self.oauth_request_payload
        token_response = requests.post(
            self.auth_endpoint,
            headers=self._oauth_headers,
            data=auth_request_payload,
            timeout=60,
        )
        try:
            token_response.raise_for_status()
        except requests.HTTPError as ex:
            msg = f"Failed OAuth login, response was '{token_response.json()}'. {ex}"
            raise RuntimeError(msg) from ex

        self.logger.info("OAuth authorization attempt was successful.")

        token_json = token_response.json()
        self.access_token = token_json["access_token"]
        # TODO: store refresh token
        self.refresh_token = token_json["refresh_token"]
        self.logger.info("OAuth refresh_token: %s", self.refresh_token)
        expiration = token_json.get("expires_in", self._default_expiration)
        self.expires_in = int(expiration) if expiration else None
        if self.expires_in is None:
            self.logger.debug(
                "No expires_in received in OAuth response and no "
                "default_expiration set. Token will be treated as if it never "
                "expires.",
            )
        self.last_refreshed = request_time
