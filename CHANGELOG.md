# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Releases](https://github.com/cancerDHC/sheet2linkml/releases)

## [Unreleased]
* Feature: added a dummy Google Sheet, the expected schema, and a test to compare them.
* Feature: cleaned up GitHub Action for style checks and added PyTest.
* Feature: added support for storing Google API credentials in an environmental variable, and added it to 
  GitHub Actions.
* Feature: added check for Google Sheet ID.
* Feature: updated @cached_property with @property @lru_cache to support Python 3.7.
* Bug: updated CCDH Terminology API endpoint for enumerations.
* Bug: fixed code to correctly handle 404 responses from the TCCM Terminology Service.

## [v1.2.0] - 2021-11-29

* Separate enums from codeable concepts

## [v1.1.1] - 2021-11-11

* Updated minimum Python version from 3.9 to 3.7, thanks to changes from v1.1.0

## [v1.1.0] - 2021-10-28

* Retroactive code style formatting of the entire codebase using Black
* Added a Github Action that checks if checked in code is Black formatted
* Modified the code to be compatible with Python versions 3.7 and 3.8 by using `typing.List` and `typing.Dict`
* Added this CHANGELOG

## [v1.0.1] - 2021-10-04

* Improved README
* Moved `python-dotenv` to list of core dependencies

## [v1.0.0] - 2021-09-30

* Added CONTRIBUTING documentation
* Package deployed to PyPI
* In its current state, it is meant to be used only as a dependency for ccdhmodel
* It is compatible with Python version 3.9 and higher

## [v0.0.1] - 2021-09-29

* First working release of `sheet2linkml`

[Unreleased]: https://github.com/cancerDHC/sheet2linkml/compare/v1.2.0...HEAD
[v1.2.0]: https://github.com/cancerDHC/sheet2linkml/compare/v1.1.1...v1.2.0
[v1.1.1]: https://github.com/cancerDHC/sheet2linkml/compare/v1.1.0...v1.1.1
[v1.1.0]: https://github.com/cancerDHC/sheet2linkml/compare/v1.0.1...v1.1.0
[v1.0.1]: https://github.com/cancerDHC/sheet2linkml/compare/v1.0.0...v1.0.1
[v1.0.0]: https://github.com/cancerDHC/sheet2linkml/compare/v0.0.1...v1.0.0
[v0.0.1]: https://github.com/cancerDHC/sheet2linkml/releases/tag/v0.0.1
