from typing import Optional
from .protocol import (
    StatusMessage,
    PlanetMessage
)
from .primitives import (
    _login,
    _get_planet,
    _get_status
)


class Credentials:

    def __init__(self, api_key: str):
        self._api_key: str = api_key
        self._token: Optional[str] = None

    @property
    def token(self) -> str:
        """Return the access token."""
        # Get a token if current one is existent or expired.
        # TODO: implement expiration detection.
        if not self._token:
            self._token = self.login(self._api_key)

        return self._token

    @staticmethod
    def login(api_key: str) -> str:
        """Login to the API and return a token."""
        return _login(api_key)


class Client:

    def __init__(self, credentials: Credentials):
        self._credentials = credentials

    @classmethod
    def from_api_key(cls, api_key: str) -> 'Client':
        """Create a Credentials object and instantiate the Client."""
        credentials = Credentials(api_key)
        return cls(credentials)

    @staticmethod
    def get_status() -> StatusMessage:
        """Return the status of the API."""
        return _get_status()

    def get_planet(self) -> PlanetMessage:
        """Return a newly generated planet."""
        return _get_planet(self._credentials.token)
