import unittest

from free_meal_inviter.app.person import Person
from free_meal_inviter.app.services import people_close_to


class TestPeopleCloseTo(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(list(people_close_to((0, 0), [], 0)), [])

    def test_noone_is_closer_than_0(self):
        people = [Person(i, f'John{i}', (20.5, 1.3)) for i in range(6)]

        self.assertEqual(list(people_close_to((0, 0), people, 0)), [])

    def test_same_coordinates_people_are_close_enough(self):
        people = [Person(i, f'John{i}', (20.5, 1.3)) for i in range(6)]

        close_people = list(people_close_to((20.5, 1.3), people, 1))
        self.assertEqual(len(close_people), 6)
