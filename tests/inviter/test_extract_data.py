import unittest
from unittest import mock

from free_meal_inviter.app.inviter import extract_data


class TestExtractData(unittest.TestCase):

    def setUp(self) -> None:
        self.json_text = ('{"latitude": "52.9875", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.071"}\n'
                          '{"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"}\n'
                          '{"latitude": "51.8856167", "user_id": 2, "name": "Ian McArdle", "longitude": "-10.4240951"}')
        self.dcts = [
            {"latitude": "52.9875", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.071"},
            {"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"},
            {"latitude": "51.8856167", "user_id": 2, "name": "Ian McArdle", "longitude": "-10.4240951"}
        ]
        self.csv_text = ('12,"Christina McArdle","52.9875","-6.071"\n'
                         '1,"Alice Cahill","51.92893","-10.27699"\n'
                         '2,"Ian McArdle","51.8856167","-10.4240951"')

    def test_wrong_format(self):
        with self.assertRaises(ValueError):
            list(extract_data('path', 'foo'))

    def test_json_format(self):
        m = mock.mock_open(read_data=self.json_text)
        with mock.patch('free_meal_inviter.app.inviter.open', m):
            dcts = list(extract_data('foo', 'json'))
            self.assertEqual(dcts[0], self.dcts[0])
            self.assertEqual(dcts[1], self.dcts[1])
            self.assertEqual(dcts[2], self.dcts[2])

    def test_json_invalid_line_in_between(self):
        json_text = self.json_text + '\n"invalid line"\n'
        json_text += self.json_text

        m = mock.mock_open(read_data=json_text)
        with mock.patch('free_meal_inviter.app.inviter.open', m):
            dcts = list(extract_data('foo', 'json'))
            self.assertEqual(len(dcts), 6)

    def test_csv_format(self):
        m = mock.mock_open(read_data=self.csv_text)
        with mock.patch('free_meal_inviter.app.inviter.open', m):
            dcts = list(extract_data('foo', 'csv'))
            for dct in dcts:
                dct['user_id'] = int(dct['user_id'])
            self.assertEqual(dcts[0], self.dcts[0])
            self.assertEqual(dcts[1], self.dcts[1])
            self.assertEqual(dcts[2], self.dcts[2])
