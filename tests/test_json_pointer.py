import unittest
from src.json_pointer import resolve_json_pointer, set_json_pointer, escape_json_pointer_token

class TestJSONPointer(unittest.TestCase):
    def test_rfc6901_resolution(self):
        doc = {
            "foo": ["bar", "baz"],
            "": 0,
            "a/b": 1,
            "c%d": 2,
            "e^f": 3,
            "g|h": 4,
            "i\\j": 5,
            "k\"l": 6,
            " ": 7,
            "m~n": 8
        }
        self.assertEqual(resolve_json_pointer(doc, ""), doc)
        self.assertEqual(resolve_json_pointer(doc, "/foo/0"), "bar")
        self.assertEqual(resolve_json_pointer(doc, "/foo/1"), "baz")
        self.assertEqual(resolve_json_pointer(doc, "/a~1b"), 1)
        self.assertEqual(resolve_json_pointer(doc, "/m~0n"), 8)

    def test_mutation(self):
        doc = {"users": [{"name": "Alice"}]}
        set_json_pointer(doc, "/users/0/name", "Bob")
        self.assertEqual(doc["users"][0]["name"], "Bob")

if __name__ == "__main__":
    unittest.main()
