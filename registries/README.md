# Registry JSON files

This directory includes JSON files containing the Registry table data for
the registries defined in DAPT.

## Structure

The JSON has the following structure:

```json
{
    "columns": [
        {
            "header": "some human readable thing",
            "isKey": true,
            "rowKey": "value",
            "isType": false
        },
        {
            "header": "some other human readable thing",
            "rowKey": "foo"
        }
    ],
    "values": [
        {
            "value": "first value",
            "foo": "bar1"
        },
        {
            "value": "second value",
            "foo": "bar2"
        }
    ]
}
```

The `header` in each object in `columns` is a human readable column header.

The `rowKey` in each object in `columns` is used as the key in each entry in
the `values` array so that the header text does not need
to be reproduced in every entry, but a simpler string can be used instead.

For each object in the `columns` array there MUST be a corresponding
key and value in every object in the `values` array.
Within the DAPT specification those values are mapped into the relevant
registry table.
Additional keys and values in a `values` array object, where the key does not
match a `rowKey` will not be reflected in the specification.

If `isKey` is `true` that indicates that the column contains a registry key.

If `isType` is `true` and `isKey` is `true` that indicates that the column
header is a data type, which will be formatted surrounded by angle brackets
as per the TTML document conventions.

## Use of the registry JSON files in DAPT implementations

Implementations can check find the set of permitted values in DAPT documents
by iterating through the `values` array, and getting the objects whose
key(s) is/are identified in `columns` with `isKey: true`.

The `status` of each value is also relevant to identify Deprecated values.
