import unittest
from src.tarjan_scc import TarjanSCC

class TestTarjanSCC(unittest.TestCase):
    def test_scc_cycles(self):
        t = TarjanSCC()
        t.add_edge("A", "B")
        t.add_edge("B", "C")
        t.add_edge("C", "A")
        t.add_edge("C", "D")
        t.add_edge("D", "E")
        t.add_edge("E", "D")

        sccs = t.find_sccs()
        sorted_sccs = sorted(sccs, key=lambda s: s[0])
        self.assertIn(["A", "B", "C"], sorted_sccs)
        self.assertIn(["D", "E"], sorted_sccs)

    def test_dag_singletons(self):
        t = TarjanSCC()
        t.add_edge("1", "2")
        t.add_edge("2", "3")
        sccs = t.find_sccs()
        self.assertEqual(len(sccs), 3)

if __name__ == "__main__":
    unittest.main()
