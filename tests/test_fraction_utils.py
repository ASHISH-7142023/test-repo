import unittest
from src.fraction_utils import RationalFraction, approximate_float

class TestFractionUtils(unittest.TestCase):
    def test_reduction(self):
        f = RationalFraction(12, 16)
        self.assertEqual(f.num, 3)
        self.assertEqual(f.den, 4)

    def test_arithmetic(self):
        a = RationalFraction(1, 2)
        b = RationalFraction(1, 3)
        self.assertEqual(a + b, RationalFraction(5, 6))
        self.assertEqual(a - b, RationalFraction(1, 6))
        self.assertEqual(a * b, RationalFraction(1, 6))
        self.assertEqual(a / b, RationalFraction(3, 2))

    def test_continued_fraction(self):
        f = RationalFraction(415, 93)
        self.assertEqual(f.to_continued_fraction(), [4, 2, 6, 7])

    def test_approximate_float(self):
        approx = approximate_float(3.14159265, max_denominator=1000)
        self.assertEqual(approx, RationalFraction(355, 113))
        approx_third = approximate_float(1/3, max_denominator=100)
        self.assertEqual(approx_third, RationalFraction(1, 3))

if __name__ == "__main__":
    unittest.main()
