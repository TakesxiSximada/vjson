#! /usr/bin/env python
# -*- coding: utf-8 -*-
import six
import sys
import json
import enum
import argparse
import jsonschema
from .compat import lru_cache


class JSONValidationError(Exception):
    pass


def before_validate(func):
    def _wrap(self, data, *args, **kwds):
        schema = self.get_schema()
        try:
            jsonschema.validate(data, schema)
        except jsonschema.ValidationError as err:
            raise JSONValidationError(err)
        return func(self, data, *args, **kwds)
    return _wrap


def after_validate(func):
    def _wrap(self, *args, **kwds):
        data = func(self, *args, **kwds)
        schema = self.get_schema()
        try:
            jsonschema.validate(data, schema)
        except jsonschema.ValidationError as err:
            raise JSONValidationError(err)
        else:
            return data
    return _wrap


class ValidatedJSON(object):
    def __init__(self, schema, isfile=False):
        self._schema = schema
        self._isfile = isfile

    @lru_cache()
    def get_schema(self):
        schema = None
        if self._isfile:
            with open(self._schema, 'rt') as fp:
                schema = fp.read()
        else:
            schema = self._schema
        return json.loads(schema) if isinstance(schema, (six.text_type, six.string_types)) else schema

    @after_validate
    def load(self, *args, **kwds):
        return json.load(*args, **kwds)

    @after_validate
    def loads(self, *args, **kwds):
        return json.loads(*args, **kwds)

    @before_validate
    def dump(self, *args, **kwds):
        return json.dump(*args, **kwds)

    @before_validate
    def dumps(self, *args, **kwds):
        return json.dumps(*args, **kwds)


class CommadExitStatus(enum.IntEnum):
    success = 0
    fail = 1


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('schema')
    parser.add_argument('json')
    parser.add_argument('--isfile', default=False, action='store_true')
    args = parser.parse_args(argv)

    vj = ValidatedJSON(args.schema, isfile=args.isfile)
    try:
        vj.loads(args.json)
    except JSONValidationError:
        return CommadExitStatus.fail.value
    else:
        return CommadExitStatus.success.value


if __name__ == '__main__':
    sys.exit(main())
