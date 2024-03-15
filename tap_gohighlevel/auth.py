"""GoHighLevel Authentication."""

from __future__ import annotations

from singer_sdk.authenticators import OAuthAuthenticator, SingletonMeta


# The SingletonMeta metaclass makes your streams reuse the same authenticator instance.
# If this behaviour interferes with your use-case, you can remove the metaclass.
class GoHighLevelAuthenticator(OAuthAuthenticator, metaclass=SingletonMeta):
    """Authenticator class for GoHighLevel."""

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
            "refresh_token": self.config["refresh_token"],
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
