# -*- coding: utf-8 -*-
import os
import json
from unittest import TestCase


def find_file(path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), path)


class ValidatedJSONTest(TestCase):
    def _get_factory(self):
        from .. import ValidatedJSON as klass
        return klass

    def _make(self, *args, **kwds):
        factory = self._get_factory()
        return factory(*args, **kwds)

    def test_load_valid(self):
        _json = self._make(find_file('data/schema.json'), isfile=True)
        obj = None
        with open(find_file('data/valid_data.json'), 'rt') as fp:
            obj = _json.load(fp)
        self.assertEqual(obj, {'name': 'Eggs', 'price': 34.99})

    def test_loads_valid(self):
        _json = self._make({
            'type': 'object',
            'properties': {
                'price': {'type': 'number'},
                'name': {'type': 'string'},
                },
            })
        obj = _json.loads('{"name" : "Eggs", "price" : 34.99}')
        self.assertEqual(obj, {'name': 'Eggs', 'price': 34.99})

    def test_load_invalid(self):
        from .. import JSONValidationError
        _json = self._make(find_file('data/schema.json'), isfile=True)
        with open(find_file('data/invalid_data.json'), 'rt') as fp:
            with self.assertRaises(JSONValidationError):
                _json.load(fp)

    def test_loads_invalid(self):
        from .. import JSONValidationError
        _json = self._make({
            'type': 'object',
            'properties': {
                'price': {'type': 'number'},
                'name': {'type': 'string'},
                },
            })

        with self.assertRaises(JSONValidationError):
            _json.loads('{"name" : "Eggs", "price" : "34.99"}')  # 34.99 is string (not a number)

    def test_dump_valid(self):
        from six import StringIO
        _json = self._make(find_file('data/schema.json'), isfile=True)
        fp = StringIO()
        _json.dump({'name': 'Eggs', 'price': 34.99}, fp)
        fp.seek(0)
        obj = _json.load(fp)
        self.assertEqual(obj, {'name': 'Eggs', 'price': 34.99})

    def test_dumps_valid(self):
        _json = self._make({
            'type': 'object',
            'properties': {
                'price': {'type': 'number'},
                'name': {'type': 'string'},
                },
            })
        txt = _json.dumps({'name': 'Eggs', 'price': 34.99})
        obj = json.loads(txt)
        self.assertEqual(obj, {'name': 'Eggs', 'price': 34.99})

    def test_dump_invalid(self):
        from six import StringIO
        from .. import JSONValidationError
        _json = self._make(find_file('data/schema.json'), isfile=True)
        fp = StringIO()
        with self.assertRaises(JSONValidationError):
            _json.dump({'name': 'Eggs', 'price': '34.99'}, fp)

    def test_dumps_invalid(self):
        from .. import JSONValidationError
        _json = self._make({
            'type': 'object',
            'properties': {
                'price': {'type': 'number'},
                'name': {'type': 'string'},
                },
            })
        with self.assertRaises(JSONValidationError):
            _json.dumps({'name': 'Eggs', 'price': '34.99'})  # 34.99 is string (not a number)
