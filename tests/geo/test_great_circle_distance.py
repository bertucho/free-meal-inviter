import math
import unittest

from hypothesis import given, strategies as st

from free_meal_inviter.app.geo import EARTH_RADIUS, great_circle_distance, Coordinates

EARTH_CIRCUMFERENCE = 2 * math.pi * EARTH_RADIUS
NORTH_POLE = (90, 0)
SOUTH_POLE = (-90, 0)


class TestGreatCircleDistance(unittest.TestCase):

    @given(st.floats(min_value=-90.0, max_value=90.0),
           st.floats(min_value=-180.0, max_value=180.0))
    def test_zero_distance(self, lat, lng):
        """Same coordinates will have a distance almost equals to zero"""
        self.assertAlmostEqual(great_circle_distance((lat, lng), (lat, lng)), 0, 3)

    @given(st.floats(min_value=-90.0, max_value=90.0),
           st.floats(min_value=-180.0, max_value=180.0),
           st.floats(min_value=-90.0, max_value=90.0),
           st.floats(min_value=-180.0, max_value=180.0))
    def test_any_distance_greater_than_or_equals_to_zero(self, lat_a, lng_a, lat_b, lng_b):
        """Any two coordinates will have a distance greater than or equals to zero"""
        self.assertGreaterEqual(great_circle_distance((lat_a, lng_a), (lat_b, lng_b)), 0)

    @given(st.floats(min_value=-90.0, max_value=90.0),
           st.floats(min_value=-180.0, max_value=180.0),
           st.floats(min_value=-90.0, max_value=90.0),
           st.floats(min_value=-180.0, max_value=180.0))
    def test_no_distance_is_greater_than_half_equator(self, lat_a, lng_a, lat_b, lng_b):
        """Any two coordinates will have a distance less than or equals to half the equator"""
        max_distance = EARTH_CIRCUMFERENCE / 2 + 1  # To avoid precision errors
        self.assertLessEqual(great_circle_distance((lat_a, lng_a), (lat_b, lng_b)), max_distance)

    def test_distance_between_poles(self):
        expected_distance = EARTH_CIRCUMFERENCE / 2
        self.assertEqual(great_circle_distance(NORTH_POLE, SOUTH_POLE), expected_distance)

    def test_half_trip_around_equator(self):
        expected_distance = EARTH_CIRCUMFERENCE / 2
        self.assertEqual(great_circle_distance((0, 0), (0, 180)), expected_distance)

    def test_equivalence_of_pos_and_neg_180_longitude(self):
        distance1 = great_circle_distance((0, -180), (0, 180))
        distance2 = great_circle_distance((0, 180), (0, -180))

        self.assertEqual(distance1, 0)
        self.assertEqual(distance2, 0)

    def test_string_coordinates(self):
        dist1 = great_circle_distance(("1", "30"), ("20", "60"))
        dist2 = great_circle_distance((1, 30), (20, 60))
        self.assertEqual(dist1, dist2)

    def test_coordinates_instances(self):
        dist1 = great_circle_distance(Coordinates("1", "30"), Coordinates("20", "60"))
        dist2 = great_circle_distance((1, 30), (20, 60))
        self.assertEqual(dist1, dist2)
