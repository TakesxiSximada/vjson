vjson

0.1.0

vjson creates an object to serialize the only of the type specified in JSONSchema. It works like a json module.

install
===========

Next, execute command.::

    $ pip install vjson


How to use
==========

You define an object using JSONSchema.::

    >>> import vjson
    >>> _json = vjson.ValidatedJSON({
    ... 'type': 'object',
    ... 'properties': {
    ...     'price': {'type': 'number'},
    ...     'name': {'type': 'string'},
    ...     },
    ... })

This object can dumps/loads()/dump()/load() the serializable object, as in the json module.::

    >>> _json.loads('{"name" : "Eggs", "price" : 34.99}')
    {'name': 'Eggs', 'price': 34.99}
    >>> _json.dumps({"name": "Eggs", "price": 34.99})
    '{"name": "Eggs", "price": 34.99}'

If you try to pass the data that violates the JSONSchema that was specified in the constructor, it raises a vjson.JSONValidationError.::

    >>> _json.loads('{"name" : "Eggs", "price" : "34.99"}')
    Traceback (most recent call last):
      File "/tmp/test/var/src/develop/vjson/src/vjson/__init__.py", line 32, in _wrap
        jsonschema.validate(data, schema)
      File "/tmp/test/env/lib/python3.4/site-packages/jsonschema/validators.py", line 478, in validate
        cls(schema, *args, **kwargs).validate(instance)
      File "/tmp/test/env/lib/python3.4/site-packages/jsonschema/validators.py", line 123, in validate
        raise error
    jsonschema.exceptions.ValidationError: '34.99' is not of type 'number'

    Failed validating 'type' in schema['properties']['price']:
        {'type': 'number'}

    On instance['price']:
        '34.99'

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/tmp/test/var/src/develop/vjson/src/vjson/__init__.py", line 34, in _wrap
        raise JSONValidationError(err)
    vjson.JSONValidationError: '34.99' is not of type 'number'

    Failed validating 'type' in schema['properties']['price']:
        {'type': 'number'}

    On instance['price']:
        '34.99'
    >>>
