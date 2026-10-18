import unittest
from src.expression_evaluator import evaluate_expression

class TestExpressionEvaluator(unittest.TestCase):
    def test_simple_eval(self):
        self.assertEqual(evaluate_expression("3 + 4 * 2"), 11.0)
        self.assertEqual(evaluate_expression("(3 + 4) * 2"), 14.0)

    def test_exponentiation(self):
        self.assertEqual(evaluate_expression("2 ^ 3 ^ 2"), 512.0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate_expression("10 / 0")

if __name__ == "__main__":
    unittest.main()
