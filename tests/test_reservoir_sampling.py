import unittest
import random
from src.reservoir_sampling import reservoir_sample

class TestReservoirSampling(unittest.TestCase):
    def test_sample_size(self):
        stream = range(100)
        sample = reservoir_sample(stream, 10, rng=random.Random(42))
        self.assertEqual(len(sample), 10)
        self.assertTrue(all(x in range(100) for x in sample))

    def test_small_stream(self):
        sample = reservoir_sample([1, 2, 3], 5)
        self.assertEqual(len(sample), 3)

if __name__ == "__main__":
    unittest.main()
