# DAPT XSD Validator

Basic command line utility for validating DAPT documents using
the XML Schema Definition in the w3c/dapt repository.

This script uses the MIT licensed [`xmlschema`](https://github.com/sissaschool/xmlschema) library.

This script is provided as-is with no warranties of any kind.
The repository's `LICENSE.md` applies, with the contents of this folder
being considered a _code example_.

## Build

1. Install poetry - [installation instructions](https://python-poetry.org/docs/#installing-with-the-official-installer)
2. Ensure you have a version of Python greater than or equal to 3.11 available
for example with the command `poetry env use 3.11`
3. Install the dependencies by running `poetry install`

## Usage

```sh
poetry run validate -dapt_in path/to/dapt_file.ttml
```

or pass the document for validating in via stdin, e.g.:

```sh
poetry run validate < path/to/dapt_file.ttml
```

## Tests

```sh
poetry run python -m unittest
```
