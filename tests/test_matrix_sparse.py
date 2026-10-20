import unittest
from src.matrix_sparse import SparseMatrix

class TestSparseMatrix(unittest.TestCase):
    def test_indexing_and_sparsity(self):
        m = SparseMatrix(100, 100)
        m[5, 5] = 42.0
        self.assertEqual(m[5, 5], 42.0)
        self.assertEqual(m[0, 0], 0.0)
        self.assertEqual(m.nnz, 1)
        self.assertEqual(m.density, 1 / 10000.0)

    def test_arithmetic(self):
        a = SparseMatrix(2, 2)
        b = SparseMatrix(2, 2)
        a[0, 0] = 1.0
        b[0, 0] = 2.0
        b[1, 1] = 5.0
        c = a.add(b)
        self.assertEqual(c[0, 0], 3.0)
        self.assertEqual(c[1, 1], 5.0)

if __name__ == "__main__":
    unittest.main()
