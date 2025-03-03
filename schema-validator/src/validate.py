import os
import sys
import argparse
import xmlschema
import logging

logging.getLogger().setLevel(logging.INFO)


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
    schema_paths = [schema_path, metadata_items_schema_path]
    logging.info('Creating schema from XSDs at {}'.format(schema_paths))
    schema = xmlschema.XMLSchema(schema_paths)
    schema.build()
    if schema.validity:
        logging.info('Schemas are valid')
    else:
        logging.error('Schemas are not valid, exiting early')
        return -1

    try:
        logging.info('Validating document at {}'.format(args.dapt_in.name))
        schema.validate(args.dapt_in)
    except xmlschema.XMLSchemaValidationError as valex:
        logging.error(str(valex))
        logging.error('Document is not valid.')
        return -1

    logging.info(
        'Document is syntactically valid with respect to the '
        'DAPT XML Schema Definition; '
        'this does not check all semantic requirements of the '
        'DAPT specification.')
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
