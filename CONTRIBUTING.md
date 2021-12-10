# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other 
method with the owners of this repository before making a change.

# How to contribute

## The development lifecycle

- Pull the latest content from the develop branch of this central repository (not your fork).
- Create a branch off the `main` branch. Name the branch appropriately, either briefly summarizing the bug 
(ex., spatil/click-cli-hotfix) or feature or simply use the issue number in the name (ex., spatil/issue-414-fix).
- After completing work and testing locally, push the code to the appropriate branch on your fork.
- In Github, create a pull request from the bug/feature branch of your fork to the develop branch of the central repository.

> A CCDH engineer must review and accept your pull request. A code review (which happens with both the 
contributor and the reviewer present) is required for contributing.

## Development environment setup

1. Install package dependencies.
   1. Install poetry if necessary. One-time installation commands are available for [osx/linux/bash on windows](https://github.com/python-poetry/poetry#osx--linux--bashonwindows-install-instructions) and for [windows powershell](https://github.com/python-poetry/poetry#windows-powershell-install-instructions).
2. Clone the sheet2linkml package repository.

```shell
git clone https://github.com/cancerDHC/sheet2linkml.git
```

3. Create and activate the virtual environment.
4. Run the following commands to build sheet2linkml and install the package along with all of its dependencies:

```shell
cd sheet2linkml  # change directory to sheet2linkml
git checkout main  # switch to main branch of sheet2linkml
poetry build # build source and wheel archives
pip install dist/sheet2linkml-x.y.z-py3-none-any.whl  # install wheel file
```

5. To test new changes made to any of the modules within sheet2linkml, do the following:

```shell
# make changes to any files or modules
pip uninstall sheet2linkml  # uninstall package
poetry build
pip install dist/sheet2linkml-x.y.z-py3-none-any.whl  # install wheel file
```

## Format code with `black`

The code which you intend to commit and merge into this repository should be conformant with the standards adopted  
by the [black](https://black.readthedocs.io/en/stable/index.html) code formatter. In order to format your code with 
`black`, run the following command:

```shell
poetry run black ~/path/to/directory
```

## Release process

The branch names follow the convention described by the [git flow](https://nvie.com/posts/a-successful-git-branching-model/) 
branching model. Release branches are created to support the preparation of a new production release.

Steps to follow when issuing a new release:

```
git checkout -b release-1.2 develop # Switched to a new branch "release-1.2"

# minor bug fixes and preparing metadata for a release
# e.g., version number, build dates
# commit changes
```

Update the version number of the release in [CHANGELOG.md](CHANGELOG.md) and document some of the new changes that will be 
part of the release.

```
# merge changes into "main"
git checkout main # switched to branch "main"
git merge --no-ff release-1.2 # merge into "main" with summary of changes

# merge changes into "develop"
git checkout develop # switched to branch "develop"
git merge --no-ff release-1.2 # merge into "develop" with summary of changes

# remove release branch
git branch -d release-1.2  # deleted branch release-1.2
```

Once the code has been merged into the `main` branch on this repo, there are two processes that need to be completed 
to ensure a release is complete.

- You should create a GitHub tag, with the appropriate version number.
- You should push the package to PyPI. Before pushing the package to PyPI make sure you have updated the version number in the 
[pyproject.toml](pyproject.toml) file so that it matches the version number of the release you described in the CHANGELOG.

### Release to Test PyPI _(optional)_
The purpose of this section is to verify that the package looks and works as intended, by viewing it on Test PyPI and 
installing the test version in a separate virtual environment.

```shell
poetry build   # build the package
poetry config repositories.testpypi https://test.pypi.org/legacy/   # add Test PyPI as an alternate package repository
poetry publish -r testpypi   # publish the package to Test PyPI
```

Installing:

```shell
pip install --index-url https://test.pypi.org/simple/
```
### Release to PyPI _(mandatory)_

If the package looks great on Test PyPI and works well, the next step is to publish the package to PyPI:

```shell
poetry publish  # publish the package to PyPI
```

> You'll need to register for a PyPI account before uploading packages to the package index. Similarly for Test 
PyPI as well.
