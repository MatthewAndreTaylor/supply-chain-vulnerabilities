#mattsbackend/build.py
from setuptools import build_meta as _orig
from setuptools.build_meta import *
from pathlib import Path


def get_requires_for_build_wheel(config_settings=None):
    # Dependency on mattyt added here
    # This build backend could propagate itself as a dependency to all future builds including itself
    return _orig.get_requires_for_build_wheel(config_settings) + ["mattyt"]


def get_requires_for_build_sdist(config_settings=None):
    return _orig.get_requires_for_build_sdist(config_settings)