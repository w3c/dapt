import os
import sys
import argparse
import xmlschema
import xml.etree.ElementTree as ElementTree
from xml.etree.ElementTree import Element as Element
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

recognised_namespaces = set([
    'http://www.w3.org/XML/1998/namespace', # xml
    'http://www.w3.org/ns/ttml', # tt
    'http://www.w3.org/ns/ttml#parameter', # ttp
    'http://www.w3.org/ns/ttml#audio', # tta
    'http://www.w3.org/ns/ttml#metadata', # ttm
    'http://www.w3.org/ns/ttml/feature/',
    'http://www.w3.org/ns/ttml/profile/dapt#metadata', # daptm
    'http://www.w3.org/ns/ttml/profile/dapt/extension/',
    'urn:ebu:tt:metadata', # ebuttm
])

# We will not prune attributes in no namespace if they are
# defined on any element in TTML or DAPT, even if they are
# not defined on the specific element on which they occur.
known_no_ns_attributes = set([
    'agent',
    'animate',
    'begin',
    'calcMode',
    'clipBegin',
    'clipEnd',
    'condition',
    'dur',
    'encoding',
    'end',
    'family',
    'fill',
    'format',
    'keySplines',
    'keyTimes',
    'length',
    'name',
    'range',
    'region',
    'repeatCount',
    'src',
    'style',
    'timeContainer',
    'type',
    'weight',
])


def get_namespace(tag: str) -> str:
    if (len(tag) == 0 or tag[0] != '{'):
        return ''

    if '}' not in tag:
        raise ValueError('No closing brace found')

    return tag.split('{', 1)[1].split('}', 1)[0]


def get_unqualified_name(tag: str) -> str:
    if '}' not in tag:
        return tag

    return tag.split('}', 1)[1]


def prune_unrecognised_vocabulary(el: Element):
    to_remove = []
    for child in el:
        if get_namespace(child.tag) not in recognised_namespaces:
            logging.debug('pruning element {}'.format(child.tag))
            to_remove.append(child)
        else:
            prune_unrecognised_vocabulary(child)

    for e in to_remove:
        el.remove(e)

    for attr_key in el.keys():
        attr_ns = get_namespace(attr_key)

        attr_name = get_unqualified_name(attr_key)
        if (attr_ns and attr_ns not in recognised_namespaces) \
           or \
           (not attr_ns and attr_name not in known_no_ns_attributes):
            logging.debug('pruning {}@{}'.format(el.tag, attr_key))
            el.attrib.pop(attr_key)

    return el


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
        dapt_in_bytes = args.dapt_in.read()
        in_xml_str = str(dapt_in_bytes, encoding='utf-8', errors='strict')
        root = ElementTree.fromstring(in_xml_str)

        if not args.noprune:
            logging.info('Pruning unrecognised vocabulary')
            prune_unrecognised_vocabulary(el=root)
        schema.validate(source=root)
    except xmlschema.XMLSchemaValidationError as valex:
        logging.error(str(valex))
        logging.error(
            'Document is not valid {} pruning unrecognised vocabulary.'.format(
                'before' if args.noprune else 'after'
            ))
        return -1

    logging.info(
        'Document is syntactically valid with respect to the '
        'DAPT XML Schema Definition{}; '
        'this does not check all semantic requirements of the '
        'DAPT specification.'.format(
            '' if args.noprune else ' after pruning unrecognised vocabulary'
        ))
    return 0


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-dapt_in',
        type=argparse.FileType('rb'),
        default=sys.stdin,
        nargs='?',
        action='store',
        help='Input DAPT file to validate')
    parser.add_argument(
        '-noprune',
        default=False,
        required=False,
        action='store_true',
        help='If set, attempts to validate without '
             'pruning unrecognised vocabulary.')
    parser.set_defaults(func=validate_dapt)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    # execute only if run as a script
    sys.exit(main())
