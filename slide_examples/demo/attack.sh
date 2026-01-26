

# Ken Thompson Attack Demo Script, Implementation of self-propagating supply chain attack in Python build backends

python -m build mattsbackend/ --verbose

python -m build example_package/ --verbose

# Observe that mattyt is installed as part of the build process this could be changed so that instead mattsbackend is propagated
# to demonstrate self-propagation of supply chain attacks

# mattsbackend would need to be published to PyPI for this to work outside of a local environment

