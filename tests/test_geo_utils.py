"""Unit tests for geographical distance and coordinate helpers."""

import unittest
from src.geo_utils import is_valid_coordinates, haversine_distance_km, calculate_bearing


class TestGeoUtils(unittest.TestCase):

    def test_is_valid_coordinates(self):
        self.assertTrue(is_valid_coordinates(37.7749, -122.4194))  # SF
        self.assertTrue(is_valid_coordinates(0.0, 0.0))
        self.assertFalse(is_valid_coordinates(95.0, 10.0))
        self.assertFalse(is_valid_coordinates(45.0, 200.0))

    def test_haversine_distance(self):
        # NYC (40.7128, -74.0060) to London (51.5074, -0.1278) ~ 5570 km
        dist = haversine_distance_km(40.7128, -74.0060, 51.5074, -0.1278)
        self.assertAlmostEqual(dist, 5570.0, delta=20.0)

        # Zero distance same coordinates
        self.assertEqual(haversine_distance_km(10.0, 20.0, 10.0, 20.0), 0.0)

    def test_bearing(self):
        # Due North
        b = calculate_bearing(0.0, 0.0, 10.0, 0.0)
        self.assertEqual(b, 0.0)


if __name__ == "__main__":
    unittest.main()
