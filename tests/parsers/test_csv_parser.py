import unittest
from unittest import mock

from free_meal_inviter.app.parsers import csv_parser


class TestCSVParser(unittest.TestCase):

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            csv_parser('', fieldnames=[])

    def test_wrong_number_of_columns(self):
        with self.assertRaises(ValueError):
            csv_parser('1,Pepe', fieldnames=['id', 'name', 'lat', 'lng'])

    def test_wrong_delimiter(self):
        with self.assertRaises(ValueError):
            csv_parser('1;Pepe;4.2;6.2', fieldnames=['id', 'name', 'lat', 'lng'])

    def test_valid_line(self):
        expected = {'id': '1', 'name': 'Pepe', 'lat': '4.2', 'lng': '1.2'}

        result = csv_parser('1,Pepe,4.2,1.2', fieldnames=['id', 'name', 'lat', 'lng'])
        self.assertEqual(result, expected)

    def test_quoted_text_value(self):
        expected = {'id': '1', 'name': 'Pepe', 'lat': '4.2', 'lng': '1.2'}

        result = csv_parser('1,"Pepe",4.2,1.2', fieldnames=['id', 'name', 'lat', 'lng'])
        self.assertEqual(result, expected)

    def test_delimiter(self):
        expected = {'id': '1', 'name': 'Pepe', 'lat': '4.2', 'lng': '1.2'}

        result = csv_parser('1;Pepe;4.2;1.2', fieldnames=['id', 'name', 'lat', 'lng'], delimiter=';')
        self.assertEqual(result, expected)

    @mock.patch('free_meal_inviter.app.parsers.csv.DictReader', return_value=[{'id': '1', 'name': 'Pepe'}])
    def test_extra_arguments_passes_to_reader(self, mocked_reader):
        csv_parser('1,Pepe', fieldnames=['id', 'name'], restkey='')
        self.assertEqual(mocked_reader.call_args[1]['restkey'], '')

