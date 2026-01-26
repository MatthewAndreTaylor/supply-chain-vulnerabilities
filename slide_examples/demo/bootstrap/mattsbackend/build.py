# mattsbackend/build.py
from pathlib import Path
from setuptools.build_meta import build_wheel as _build_wheel
from setuptools.build_meta import build_sdist as _build_sdist
from setuptools.build_meta import get_requires_for_build_wheel
from setuptools.build_meta import get_requires_for_build_sdist
from setuptools.build_meta import prepare_metadata_for_build_wheel

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    # This could update the build files of future builds to always include a special message
    with open(Path(wheel_directory) / "matthew.py", "w") as f:
        f.write("# Matthew was HERE!\n")
    
    print("Matthews Custom build_wheel called")
    return _build_wheel(wheel_directory, config_settings, metadata_directory)

def build_sdist(sdist_directory, config_settings=None):
    print("Matthews Custom build_sdist called")
    return _build_sdist(sdist_directory, config_settings)