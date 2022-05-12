.. Typer documentation master file, created by
   sphinx-quickstart on Mon Feb 21 11:08:12 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Planet Generator SDK
====================

Official Python SDK of `Planet API`_

Planet API is a 2D planet sprite generator. Our internal process procedurally generate surfaces, map them to a true sphere, to finally render a planet at 1080x1080 with transparent background.
This SDK facilitate the interaction with the API and implement masks features to add lighting and solar effect to the planets.

This API currently under development. During this phase, it can be accessed for free. Request an `API key over here`_.

.. toctree::
   :maxdepth: 1
   :caption: Getting Started

   started/install
   started/quickstart
   started/about

Python API
##########

.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :caption: Python API
   :recursive:

   planet_generator.client

Indices and tables
##################

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Planet API: https://planet.joffreybvn.be/
.. _API key over here: https://discord.gg/SEGApgznjq