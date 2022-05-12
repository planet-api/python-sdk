from dataclasses import dataclass
from typing import Optional
from urllib.request import urlopen
from PIL import Image
from .config import config


@dataclass
class Shape:
    """Image shape."""
    width: Optional[int] = 1000
    height: Optional[int] = 1000


def load_mask(image_name: str) -> Image:
    """Load a mask from remote server."""
    return Image.open(urlopen(f"https://{config.assets_endpoint}/masks/{image_name}"))


class PlanetSprite:

    # Load masks from API
    shadow_mask: Image = load_mask("shadow_mask.png")
    transparency_mask: Image = load_mask("transparency_mask.png")
    atmosphere_mask: Image = load_mask("atmosphere.png")

    def __init__(self, image_url: str):
        self._image = Image.open(urlopen(image_url))
        self._size = Shape(self._image.width, self._image.height)

    def get_image(self, apply_masks: bool = False) -> Image:
        """Get the sprite image."""
        if apply_masks:
            self.apply_masks()
        return self._image

    def apply_masks(
            self,
            shadow: bool = True,
            transparency: bool = True,
            atmosphere: bool = True,
            down_sample: bool = True
    ) -> None:
        """Apply masks and down sample."""

        # Apply masks
        if shadow:
            self._image = self._apply_shadow(self._image, self._size)
        if transparency:
            self._image = self._apply_transparency(self._image, self._size)
        if atmosphere:
            self._image = self._apply_atmosphere(self._image, self._size)

        # Down sample and return
        if down_sample:
            self._downsample(self._image, self._size)

    def _apply_shadow(self, image: Image, size: Shape) -> Image:
        """Apply shadow mask to the image."""

        shadow = Image.new('RGB', (size.width, size.height))
        shadow.paste(image, mask=self.shadow_mask)
        return shadow

    def _apply_transparency(self, image: Image, size: Shape) -> Image:
        """Give transparency to the image."""

        transparency = Image.new('RGBA', (size.width, size.height))
        transparency.paste(image, mask=self.transparency_mask)
        return transparency

    def _apply_atmosphere(self, image: Image, size: Shape) -> Image:
        """Add atmosphere to the planet."""

        atmosphere = Image.new('L', (size.width, size.height))
        atmosphere.paste(self.atmosphere_mask)
        image.paste(self.atmosphere_mask, mask=atmosphere)
        return image

    @staticmethod
    def _downsample(image: Image, size: Shape) -> Image:
        """Down sample image by two."""
        return image.resize(
            (size.width // 2, size.height // 2),
            Image.Resampling.LANCZOS
        )
