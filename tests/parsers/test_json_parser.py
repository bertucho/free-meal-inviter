import json
import unittest
from unittest import mock

from free_meal_inviter.app.parsers import json_parser


class TestJSONParser(unittest.TestCase):

    def test_empty_string(self):
        with self.assertRaises(json.JSONDecodeError):
            json_parser('')

    def test_string(self):
        elem = '"some string"'

        with self.assertRaises(ValueError):
            json_parser(elem)

    def test_object(self):
        elem = '{"id": 5, "name": "Pepe"}'
        expected = {"id": 5, "name": "Pepe"}

        self.assertEqual(json_parser(elem), expected)

    def test_nested_objects(self):
        elem = '{"id": 5, "name": "Pepe", "address": {"road": "Pearse St.", "number": 15}}'
        expected = {"id": 5, "name": "Pepe", "address": {"road": "Pearse St.", "number": 15}}

        self.assertEqual(json_parser(elem), expected)

    def test_list(self):
        elem = '[{"id": 1}, {"id": 2}]'

        with self.assertRaises(ValueError):
            json_parser(elem)

    def test_invalid_elem(self):
        elem = {'id': 1, 'name': 'Pepe'}

        with self.assertRaises(TypeError):
            json_parser(elem)

    @mock.patch('free_meal_inviter.app.parsers.json.loads', return_value={})
    def test_extra_arguments_passes_to_json_loads(self, mocked_loads):
        class Foo:
            pass

        json_parser('foo', cls=Foo)

        mocked_loads.assert_called_with('foo', cls=Foo)
