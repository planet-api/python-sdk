# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Load the library version
library_variables = {}
with open(path.join(HERE, "planet_generator/_version.py")) as f:
    exec(f.read(), library_variables)

# This call to setup() does all the work
setup(
    name="planet-generator-sdk",
    version=library_variables['__version__'],
    description="Python SDk for Planet API, the 2D planet sprite generator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://planet.joffreybvn.be",
    author="Joffrey Bienvenu",
    author_email="joffreybvn@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(exclude=['docs', 'notebooks', 'scripts', 'tests']),
    include_package_data=True,
    install_requires=["Pillow"]
)
