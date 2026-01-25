# Supply Chain Vulnerabilities

<img alt='Python' src='https://img.shields.io/badge/Python-100000?style=flat&logo=Python&logoColor=FFFFFF&labelColor=black&color=black'/>


The goal of this lab is to detect and respond to software supply chain vulnerabilities.
In this lab we will primarily be using Python, but similar concepts apply across other supply chains.

Learning goals

- Understand how search and find vulnerabilities in example packages.
- Update packages and write commands to safely download packages.
- Create and understand the purpose of a lockfile [uv.lock](https://docs.astral.sh/uv/concepts/projects/layout/#the-lockfile) for protecting supply chain security.
- Understand how automated tools detect vulnerabilities ahead of releases.

**By learning how to audit, look for vulnerabilities and use secure installs yourself the hope is that you will understand how tools that protect supply chain security work**

The vunerability put into each package is that it installs another package named `mattyt`. Similar to a russian nesting doll. 🎎

As good actors we encourage you to look at the package that will be installed in the examples. https://pypi.org/project/mattyt/

The source code is here https://github.com/MatthewAndreTaylor/CSC427-mpackage-example (Only contains a `README.md`)

Fill out `notes.txt` for each written task.



# Submission

A completed `notes.txt`

The updated `awesome_mathutils` source package `awesome_mathutils-{version}.tar.gz`

The `awesome_requests/pyproject.toml` and `awesome_requests/uv.lock`


# Prerequisites

- Install [Python >= 3.11](https://www.python.org/downloads/)
- Install [uv](https://github.com/astral-sh/uv)

# Tasks


## Task 1

- Take a look through the `awesome_mathutils` package

- Run `pip install ./awesome_mathutils` 

This will build and install `awesome_mathutils`, but also secretly installs `mattyt`. You can verify this with the following

```sh
pip show mattyt
```

If it was installed you will see something similar 

```
Name: mattyt
Version: 69.69.69
Location: C:\Users\...\site-packages
```


### Task 1.1 - detection

Matthew the maintainer has accidentally approved a pull request which secretly installs the package `mattyt` in two places.


(a) Write out the function call which is executed to install the `mattyt` package for source distributions

(b) Write out the function call which is executed to install the `mattyt` package for binary distributions

hint: 🐶


### Task 1.2 - remediation

(a) Update setup.py removing any unsafe code

(b) Create a pyproject.toml removing dynamic dependencies, add setuptools as the build backend. (https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

(c) Include only the dog image properly. (https://setuptools.pypa.io/en/latest/userguide/datafiles.html#package-data)

(d) Bump the version by one patch (https://semver.org/) and add yourself as an author.

Build the wheel file save this it is what you will upload.

`python ./awesome_mathutils/setup.py sdist`


## Task 2

- Take a look through the `awesome_requests` package

- Run `pip install ./awesome_requests`

This will build and install `awesome_requests`, but also install the `mattyt` package from PyPI


### Task 2.1 - package source

hint: [finding pip packages](https://pip.pypa.io/en/stable/cli/pip_install/#finding-packages)

(a) Write a command with `pip` to install `requests` specifically from github `https://github.com/psf/requests` 

(b) Write a command with `pip` to install `requests` from github `https://github.com/psf/requests` falls back onto PyPI `https://pypi.org/simple`.

(c) Write a command with `pip` to install `awesome_requests` without package dependencies.


### Task 2.2 - lockfile

With `uv`, hashes are first-class, not optional. `uv` treats the lockfile as a cryptographic manifest. Protecting against manipulated package downloads and mirror repositories.

(a) Add secure versions to the dependencies used in the package, remove any potentially vunerable build requirements.

(b) Update the dependency `requests` to use github `https://github.com/psf/requests` as the source. Assume PyPI has been corrupted, use the tagged commit from the following release `https://github.com/psf/requests/releases/tag/v2.32.4`

(c) Update the dependency `mattyt` to use the safe local version.

(d) Bump the version by one patch see: (https://semver.org/) and add yourself as an author.

(e) Create a `uv.lock` file. see: (https://docs.astral.sh/uv/guides/projects/#uvlock)

(f) Install `uv-secure` is a tool that checks for known vulnerabilities listed against those packages and versions in the PyPi json API.

```
uv tool install uv-secure
uv-secure
```

paste the output into `notes.txt`


## Task 3

This section will have you go through an example of security auditing packages using tools.


### Task 3.1 - tools

(a) List 4 addtional example auditing tools which check for possible supply chain vulnerabilities. Write an example command for each.

Along with the command also write how the tool works: (checks vulnerable versions against a database, static analysis of code, hash/signature verification, monitors build pipeline, continuous runtime correlation, etc.)


### Task 3.2 - ci

(a) Look through the workflow `.github\workflows\python-publish.yml` find out where this shared code is run. 

Paste a link to the pyproject.toml artifact produced by the job. Might it be useful to scan through the other artifacts of the build before publishing?


(b) Write the name of the step in the workflow that adds a dependency to `awesome_requests` when making a release.
