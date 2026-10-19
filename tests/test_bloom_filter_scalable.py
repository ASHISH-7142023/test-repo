import unittest
from src.bloom_filter_scalable import ScalableBloomFilter

class TestScalableBloomFilter(unittest.TestCase):
    def test_basic_membership(self):
        sbf = ScalableBloomFilter(initial_capacity=10, error_rate=0.01)
        items = [f"item_{i}" for i in range(50)]
        for item in items:
            sbf.add(item)
        for item in items:
            self.assertIn(item, sbf)
        self.assertNotIn("non_existent_random_key_9999", sbf)
        self.assertGreater(sbf.num_filters, 1)
        self.assertEqual(len(sbf), 50)

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):
            ScalableBloomFilter(initial_capacity=0)
        with self.assertRaises(ValueError):
            ScalableBloomFilter(error_rate=1.5)

if __name__ == "__main__":
    unittest.main()
