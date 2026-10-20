import unittest
from src.geo_distance import initial_bearing, destination_point, haversine_distance_km

class TestGeoDistance(unittest.TestCase):
    def test_bearing(self):
        b = initial_bearing(0.0, 0.0, 10.0, 0.0)
        self.assertAlmostEqual(b, 0.0, places=1)
        b_east = initial_bearing(0.0, 0.0, 0.0, 10.0)
        self.assertAlmostEqual(b_east, 90.0, places=1)

    def test_destination_and_distance(self):
        start = (40.7128, -74.0060)
        dest = destination_point(start[0], start[1], 100.0, 0.0)
        dist = haversine_distance_km(start[0], start[1], dest[0], dest[1])
        self.assertAlmostEqual(dist, 100.0, delta=0.5)

if __name__ == "__main__":
    unittest.main()
