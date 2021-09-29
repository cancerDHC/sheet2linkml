# sheet2linkml
A python package for converting the CRDC-H data model, which is currently stored in a 
[Google Sheet](https://docs.google.com/spreadsheets/d/1oWS7cao-fgz2MKWtyr8h2dEL9unX__0bJrWKv6mQmM4/). The command line utility built into the package can be used 
to generate a [LinkML](https://github.com/linkml/linkml) representation of the CRDC-H data model.

## Installation Requirements and Pre-requisites

- Python 3.7.1 or higher
- [poetry](https://github.com/python-poetry/poetry)

## Installing

Create and activate a virtual environment within which you can install the package:

```shell
python -m venv .venv
source .venv/bin/activate
```

Install and update the package using pip:

```shell
poetry build
pip install dist/sheet2linkml-1.0.0-py3-none-any.whl
```

## Command Line Client Usage

```shell
sheet2linkml --output ~/path/to/crdch_model.yaml --loging-config ~/path/to/logging.ini
```
