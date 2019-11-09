import unittest

from free_meal_inviter.app.person import Person


class TestPerson(unittest.TestCase):

    def test_from_dict(self):
        dct = {'user_id': 1, 'name': 'Pepe', 'latitude': '3.2', 'longitude': '-1.1'}

        person = Person.from_dict(dct)

        self.assertEqual(person.coordinates, (3.2, -1.1))
        self.assertEqual(person.name, 'Pepe')
        self.assertEqual(person.user_id, 1)

    def test_invalid_dct(self):
        dct = {'user_id': 1, 'name': 'Pepe'}

        with self.assertRaises(KeyError):
            Person.from_dict(dct)
            Person.from_dict({})
