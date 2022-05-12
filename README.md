
# Planet Generator - Python SDK

Planet API is a **2D planet sprite generator**. Our internal process procedurally generate surfaces, map them to a true sphere, to finally render a planet at 1080x1080 with transparent background.
This SDK facilitate the interaction with the API and implement masks features to add lighting and solar effect to the planets.

This API currently under development. During this phase, it can be accessed for free. [See here how to get your key](https://planet.joffreybvn.be/).

## Installation

```shell
  pip install planet-generator-sdk
```

## Quickstart

Generate a 2D planet sprite with masks:

```python
from planet_generator import Client

# Create a Planet API client
planet_api = Client.from_api_key(
    api_key="YOUR API KEY HERE"
)

# Generate a new planet
planet = planet_api.get_planet()
sprite = planet.sprite.get_image(apply_masks=True)

sprite  # Contains the 2D planet sprite
```

