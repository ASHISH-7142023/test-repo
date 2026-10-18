import unittest
from src.topological_kahns import kahns_topological_sort

class TestTopologicalKahns(unittest.TestCase):
    def test_dag_ordering(self):
        edges = [("A", "C"), ("B", "C"), ("C", "D")]
        order, has_cycle = kahns_topological_sort(edges)
        self.assertFalse(has_cycle)
        self.assertTrue(order.index("A") < order.index("C"))
        self.assertTrue(order.index("C") < order.index("D"))

    def test_cycle_detection(self):
        edges = [("A", "B"), ("B", "C"), ("C", "A")]
        order, has_cycle = kahns_topological_sort(edges)
        self.assertTrue(has_cycle)

if __name__ == "__main__":
    unittest.main()
