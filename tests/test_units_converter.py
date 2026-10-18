import unittest
from src.units_converter import convert_length, convert_weight, convert_temperature, convert_bytes

class TestUnitsConverter(unittest.TestCase):
    def test_length(self):
        self.assertAlmostEqual(convert_length(1, "km", "m"), 1000.0)
        self.assertAlmostEqual(convert_length(1, "mi", "ft"), 5280.0)

    def test_weight(self):
        self.assertAlmostEqual(convert_weight(1, "kg", "g"), 1000.0)
        self.assertAlmostEqual(convert_weight(1, "lb", "oz"), 16.0)

    def test_temperature(self):
        self.assertAlmostEqual(convert_temperature(0, "C", "F"), 32.0)
        self.assertAlmostEqual(convert_temperature(100, "C", "F"), 212.0)
        self.assertAlmostEqual(convert_temperature(0, "C", "K"), 273.15)

    def test_bytes(self):
        self.assertEqual(convert_bytes(1, "GB", "MB"), 1024.0)

if __name__ == "__main__":
    unittest.main()
