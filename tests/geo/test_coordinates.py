import unittest

from free_meal_inviter.app.geo import Coordinates


class TestCoordinates(unittest.TestCase):

    def test_strings(self):
        coord = Coordinates('2.643', '-6.343')

        self.assertEqual(coord.lat, 2.643)
        self.assertEqual(coord.lng, -6.343)

    def test_numbers(self):
        coord = Coordinates(2, -6.343)

        self.assertEqual(coord.lat, 2)
        self.assertEqual(coord.lng, -6.343)

    def test_equality_of_objects(self):
        self.assertEqual(Coordinates('2.643', '-6.343'), Coordinates('2.643', '-6.343'))

    def test_equality_with_tuple(self):
        self.assertEqual(Coordinates('2.643', '-6.343'), (2.643, -6.343))

    def test_equality_with_iterable(self):
        gen = (i for i in (2.643, -6.343))  # gen will be a generator
        self.assertEqual(Coordinates('2.643', '-6.343'), gen)

    def test_inequality_of_objects(self):
        self.assertNotEqual(Coordinates('2.643432', '-6.343'), Coordinates('2.643', '-6.343'))
        self.assertNotEqual(Coordinates('2.643', '-6.343523'), Coordinates('2.643', '-6.343'))

    def test_inequality_with_string_tuple(self):
        self.assertNotEqual(Coordinates('2.643', '-6.343'), ('2.643', '-6.343'))

    def test_inequality_with_tuple(self):
        self.assertNotEqual(Coordinates('2.643', '-6.343'), (0, -6.343))

    def test_inequality_with_larger_tuple(self):
        self.assertNotEqual(Coordinates('2.643', '-6.343'), (2.643, -6.343, 0))

    def test_suscriptable(self):
        coord = Coordinates(2, -6.343)

        self.assertEqual(coord[0], 2)
        self.assertEqual(coord[1], -6.343)

    def test_slice(self):
        coord = Coordinates(2, -6.343)

        self.assertEqual(coord[:1], (2,))

    def test_iterable(self):
        coords = [coord for coord in Coordinates(2, -6.343)]
        self.assertEqual([2, -6.343], coords)

    def test_unpacking(self):
        lat, lng = Coordinates(2, -6.343)

        self.assertEqual(lat, 2)
        self.assertEqual(lng, -6.343)

    def test_invalid_coordinates(self):
        with self.assertRaises(ValueError):
            Coordinates(95.23, 0)

        with self.assertRaises(ValueError):
            Coordinates(0, 181.0)
