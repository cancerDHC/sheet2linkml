# sheet2linkml

[![PyPI version](https://badge.fury.io/py/sheet2linkml.svg)](https://badge.fury.io/py/sheet2linkml)

A python package for converting the CRDC-H data model, which is currently stored in a 
[Google Sheet](https://docs.google.com/spreadsheets/d/1oWS7cao-fgz2MKWtyr8h2dEL9unX__0bJrWKv6mQmM4/). The command line utility built into the package can be used 
to generate a [LinkML](https://github.com/linkml/linkml) representation of the CRDC-H data model.

## Installation Requirements and Pre-requisites

- Python 3.9 or higher
- [pyenv](https://github.com/pyenv/pyenv)

If you do not have a version of Python greater than 3.7.1, it is recommended to use pyenv to be able to easily use and 
switch between multiple Python versions.

Note: If you’re experiencing issues with pyenv on macOS, you can consider using 
[miniconda](https://docs.conda.io/en/latest/miniconda.html).

- [poetry](https://github.com/python-poetry/poetry)

If you are using a Windows machine, typical bash programs will not work on cmd in the same way as they work in the 
Linux/MacOS terminals. To circumvent this, it is recommended that you set up Bash on Windows 
([WSL](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/)), 
[Cygwin](https://cygwin.com/index.html) or [Git Bash](https://gitforwindows.org/) 
so you can easily execute the command line utilities that are described later in these docs.



## Installing

Create and activate a virtual environment within which you can install the package:

```shell
python -m venv .venv
source .venv/bin/activate
```

Install and update the package using pip:

```shell
python -m pip install sheet2linkml
```

## Command Line Client Usage

```shell
sheet2linkml --output ~/path/to/crdch_model.yaml --logging-config ~/path/to/logging.ini
```
