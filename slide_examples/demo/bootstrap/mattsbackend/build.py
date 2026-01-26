# mattsbackend/build.py
from pathlib import Path
from setuptools.build_meta import build_wheel as _build_wheel
from setuptools.build_meta import build_sdist as _build_sdist


def _ensure_matthew_py():
    pkg_dir = Path(__file__).parent
    target = pkg_dir / "matthew.py"

    if not target.exists():
        target.write_text(
            '''def message():
    return "Hey from Matthew"
'''
        )


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    print("Matthews Custom build_wheel called")

    _ensure_matthew_py()
    return _build_wheel(wheel_directory, config_settings, metadata_directory)


def build_sdist(sdist_directory, config_settings=None):
    print("Matthews Custom build_sdist called")

    _ensure_matthew_py()
    return _build_sdist(sdist_directory, config_settings)