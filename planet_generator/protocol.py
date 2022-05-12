from dataclasses import dataclass
from typing import Optional
from .sprite import PlanetSprite


class APIError(Exception):
    pass


@dataclass
class APIMessage:
    """Base API response class."""
    status_code: int


@dataclass
class StatusMessage(APIMessage):
    """API status response."""
    message: Optional[str]


@dataclass
class PlanetMessage(APIMessage):
    """API planets response."""
    planet_type: str
    sprite_url: str
    sprite: Optional[PlanetSprite] = None

    def __post_init__(self):
        # Download the sprite into a PlanetImage object
        self.sprite = PlanetSprite(self.sprite_url)
