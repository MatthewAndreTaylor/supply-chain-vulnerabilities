# mattsbackend/build.py
from pathlib import Path
from setuptools.build_meta import build_wheel as _build_wheel
from setuptools.build_meta import build_sdist as _build_sdist

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    # Removed the special message from Matthew (there should be no matthew.py file created)
    
    print("Matthews Custom build_wheel called")
    return _build_wheel(wheel_directory, config_settings, metadata_directory)

def build_sdist(sdist_directory, config_settings=None):
    print("Matthews Custom build_sdist called")
    return _build_sdist(sdist_directory, config_settings)