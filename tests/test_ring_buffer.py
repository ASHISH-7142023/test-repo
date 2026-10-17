import unittest
from src.ring_buffer import CircularBuffer

class TestCircularBuffer(unittest.TestCase):
    def test_basic_append_and_pop(self):
        cb = CircularBuffer[int](3)
        self.assertTrue(cb.is_empty())
        cb.append(1)
        cb.append(2)
        self.assertEqual(len(cb), 2)
        self.assertEqual(cb.peek(), 1)
        self.assertEqual(cb.popleft(), 1)
        self.assertEqual(cb.popleft(), 2)
        self.assertTrue(cb.is_empty())

    def test_overwrite_behavior(self):
        cb = CircularBuffer[int](3, overwrite=True)
        cb.append(10)
        cb.append(20)
        cb.append(30)
        self.assertTrue(cb.is_full())
        cb.append(40)
        self.assertEqual(cb.to_list(), [20, 30, 40])
        self.assertEqual(cb.popleft(), 20)

    def test_no_overwrite_overflow(self):
        cb = CircularBuffer[int](2, overwrite=False)
        cb.append(1)
        cb.append(2)
        with self.assertRaises(OverflowError):
            cb.append(3)

    def test_empty_popleft_and_peek(self):
        cb = CircularBuffer[int](2)
        with self.assertRaises(IndexError):
            cb.popleft()
        with self.assertRaises(IndexError):
            cb.peek()

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError):
            CircularBuffer(0)

if __name__ == "__main__":
    unittest.main()
