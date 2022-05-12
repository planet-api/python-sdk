import json
import platform as ptf
import http.client
from http.client import HTTPResponse
from typing import Optional, Dict
from ..config import config
from ..protocol import (
    StatusMessage,
    PlanetMessage
)


class _Request:

    user_agent = f'SDK Python {ptf.python_version()} {ptf.system()} {ptf.release()}'

    @classmethod
    def execute(
            cls,
            method: str,
            endpoint: str,
            auth_token: Optional[str] = None,
            content: Optional[dict] = None
    ) -> HTTPResponse:
        """Execute a GET or POST request to the API."""

        # Setup connection
        connection = http.client.HTTPSConnection(config.api_endpoint)
        body: Optional[str] = None
        headers: Dict[str, str] = {
            'User-Agent': cls.user_agent
        }

        # Add authorization header
        if auth_token:
            headers['Authorization'] = f"Bearer {auth_token}"

        # Implement POST specific parameters
        if method == 'POST' and content:
            body = json.dumps(content)
            headers['Content-Type'] = 'application/json'

        # Execute the request and return the response
        connection.request(method, endpoint, body, headers)
        return connection.getresponse()


def _login(api_key: str) -> str:
    """Login to the API and return a token."""

    # Send a login request
    response: HTTPResponse = _Request.execute(
        method='POST',
        endpoint='/login',
        content={
            "api_key": api_key
        }
    )

    # Get back the token
    data = response.read()
    return json.loads(data)['token']


def _get_status() -> StatusMessage:
    """Return the status of the API."""

    # Send a status request
    response: HTTPResponse = _Request.execute(
        method='GET',
        endpoint='/status',
    )

    # Get back the response
    data = response.read()
    message = json.loads(data)['message']

    # Return the status
    return StatusMessage(
        status_code=response.getcode(),
        message=message
    )


def _get_planet(auth_token: str) -> PlanetMessage:
    """Return a newly generated planet."""

    # Send a planet request
    response: HTTPResponse = _Request.execute(
        method='GET',
        endpoint='/planets',
        auth_token=auth_token
    )

    # Get back the response
    data = response.read()
    content = json.loads(data)

    # Return the sprite
    return PlanetMessage(
        status_code=response.getcode(),
        planet_type=content["type"],
        sprite_url=content["sprite_url"]
    )
