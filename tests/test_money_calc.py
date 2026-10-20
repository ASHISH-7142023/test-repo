import unittest
from src.money_calc import Money

class TestMoneyCalc(unittest.TestCase):
    def test_arithmetic(self):
        m1 = Money.from_float(10.50, "USD")
        m2 = Money.from_float(4.25, "USD")
        m3 = m1 + m2
        self.assertEqual(m3.amount, 14.75)

    def test_fair_split(self):
        total = Money.from_float(10.00, "USD")
        parts = total.split(3)
        self.assertEqual(len(parts), 3)
        self.assertEqual(parts[0].units, 334)
        self.assertEqual(parts[1].units, 333)
        self.assertEqual(parts[2].units, 333)
        self.assertEqual(sum(p.units for p in parts), total.units)

if __name__ == "__main__":
    unittest.main()
