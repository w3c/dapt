# DAPT XSD Validator

Basic command line utility for validating DAPT documents using
the XML Schema Definition in the w3c/dapt repository.

This script uses the MIT licensed [`xmlschema`](https://github.com/sissaschool/xmlschema) library.

This script is provided as-is with no warranties of any kind.
The repository's `LICENSE.md` applies, with the contents of this folder
being considered a _code example_.

## Build

1. Install a python build and launch tool such as:
  1. poetry - [installation instructions](https://python-poetry.org/docs/#installing-with-the-official-installer) or
  2. uv - [installation instructions](https://docs.astral.sh/uv/getting-started/installation/)
2. Ensure you have a version of Python greater than or equal to 3.11 available
for example with the command `poetry env use 3.11` or `uv python install 3.11 && uv python pin 3.11.13` (check current available versions first)
3. Install the dependencies by running `poetry install` or `uv build`

## Usage

Replacing `$launchtool` with `poetry` or `uv` according to your environment:

```sh
$launchtool run validate -dapt_in path/to/dapt_file.ttml
```

or pass the document for validating in via stdin, e.g.:

```sh
$launchtool run validate < path/to/dapt_file.ttml
```

### Validating without pruning unrecognised vocabulary

By default this script prunes unrecognised vocabulary before
XSD validation, as required by
[DAPT §5.2.1 Unrecognised vocabulary](https://www.w3.org/TR/dapt/#unrecognised-elements-and-attributes);
this behaviour can be disabled via the command line parameter
`-noprune`.


## Tests

```sh
$launchtool run python -m unittest
```
