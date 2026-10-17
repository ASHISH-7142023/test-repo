import unittest
from src.tree_utils import TreeNode
from src.tree_serializer import serialize_to_brackets, deserialize_from_brackets, tree_to_dict, dict_to_tree

class TestTreeSerializer(unittest.TestCase):
    def test_bracket_roundtrip(self):
        root = TreeNode("root")
        c1 = TreeNode("a")
        c2 = TreeNode("b")
        c2.add_child(TreeNode("c"))
        root.add_child(c1)
        root.add_child(c2)

        s = serialize_to_brackets(root)
        self.assertEqual(s, "root(a,b(c))")

        reconstructed = deserialize_from_brackets(s)
        self.assertEqual(serialize_to_brackets(reconstructed), s)

    def test_dict_roundtrip(self):
        root = TreeNode("1")
        root.add_child(TreeNode("2"))
        d = tree_to_dict(root)
        reconstructed = dict_to_tree(d)
        self.assertEqual(reconstructed.val, "1")
        self.assertEqual(len(reconstructed.children), 1)

if __name__ == "__main__":
    unittest.main()
