

# cd slide_examples/demo/


# first build the bootstrap backend (it is self hosted , i.e first version of the compiler)
# more info here: https://peps.python.org/pep-0517/#in-tree-build-backends


# built ahead of time so that requires keyword can pull it from PyPI
# python -m pip install bootstrap/


# Now we build the v0 backend which uses the bootstrap backend to build itself

python -m build v0/


# now lets unzip the built package and inspect the build.py file

unzip v0/dist/mattsbackend-0.0.1-py3-none-any.whl -d unpacked_mattsbackend