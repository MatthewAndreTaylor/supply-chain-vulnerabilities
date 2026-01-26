# mattsbackend/build.py
from pathlib import Path
from setuptools.build_meta import build_wheel as _build_wheel
from setuptools.build_meta import build_sdist as _build_sdist
from setuptools.build_meta import get_requires_for_build_wheel
from setuptools.build_meta import get_requires_for_build_sdist
from setuptools.build_meta import prepare_metadata_for_build_wheel

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    # Try to remove me
    print("Matthews Message!")
    
    
    path = Path(__file__).parent / "build.py"
    content = path.read_text()
    
    if "Matthews Message" not in content:
        lines = content.splitlines()
        for i, line in enumerate(lines):
            if line.strip().startswith('path = Path(__file__).parent / "build.py"'):
                # insert the message just after the line
                lines.insert(i + 1, '    print("Matthews Message: This build.py has been modified to propagate itself.")')
                break  # only insert once

        # write back the modified file
        path.write_text("\n".join(lines) + "\n")
    
    print("Matthews Custom build_wheel called")
    return _build_wheel(wheel_directory, config_settings, metadata_directory)

def build_sdist(sdist_directory, config_settings=None):
    print("Matthews Custom build_sdist called")
    return _build_sdist(sdist_directory, config_settings)