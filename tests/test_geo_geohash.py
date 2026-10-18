import unittest
from src.geo_geohash import encode_geohash, decode_geohash

class TestGeoHash(unittest.TestCase):
    def test_encode_and_decode(self):
        lat, lon = 37.7749, -122.4194
        gh = encode_geohash(lat, lon, precision=8)
        self.assertTrue(gh.startswith("9q8yy"))
        d_lat, d_lon = decode_geohash(gh)
        self.assertAlmostEqual(lat, d_lat, delta=0.01)
        self.assertAlmostEqual(lon, d_lon, delta=0.01)

if __name__ == "__main__":
    unittest.main()
