"""Unit tests for 2D matrix utilities."""

import unittest
from src.matrix_utils import transpose, rotate_90_clockwise, identity_matrix, matrix_multiply


class TestMatrixUtils(unittest.TestCase):

    def test_transpose(self):
        m = [[1, 2, 3], [4, 5, 6]]
        t = transpose(m)
        self.assertEqual(t, [[1, 4], [2, 5], [3, 6]])

    def test_rotate_90_clockwise(self):
        m = [[1, 2], [3, 4]]
        r = rotate_90_clockwise(m)
        self.assertEqual(r, [[3, 1], [4, 2]])

    def test_identity_matrix(self):
        i3 = identity_matrix(3)
        self.assertEqual(i3, [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])

    def test_matrix_multiply(self):
        a = [[1, 2], [3, 4]]
        b = [[2, 0], [1, 2]]
        res = matrix_multiply(a, b)
        self.assertEqual(res, [[4.0, 4.0], [10.0, 8.0]])


if __name__ == "__main__":
    unittest.main()
