import os
import sys
import argparse
import xmlschema


schema_path = os.path.normpath(
    os.path.join(
        os.path.dirname(__file__),
        '../../xml-schemas/dapt.xsd')
)
metadata_items_schema_path = os.path.normpath(
    os.path.join(
        os.path.dirname(__file__),
        '../../xml-schemas/ttml2-metadata-items.xsd')
)


def validate_dapt(args):
    # xmlschema gets baffled following the import of metadata_items,
    # so make it load it explicitly instead, which seems to work.
    schema = xmlschema.XMLSchema([schema_path, metadata_items_schema_path])
    schema.build()

    try:
        schema.validate(args.dapt_in)
    except xmlschema.XMLSchemaValidationError as valex:
        print(str(valex))
        return -1

    return 0


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-dapt_in',
        type=argparse.FileType('rb'),
        default=sys.stdin, nargs='?',
        help='Input DAPT file to validate',
        action='store')
    parser.set_defaults(func=validate_dapt)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    # execute only if run as a script
    sys.exit(main())
