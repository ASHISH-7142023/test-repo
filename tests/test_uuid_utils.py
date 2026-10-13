"""Unit tests for UUID generation, transformation, and validation."""

import unittest
from src.uuid_utils import (
    generate_uuid4,
    generate_uuid5,
    is_valid_uuid,
    short_uuid,
    expand_short_uuid
)


class TestUuidUtils(unittest.TestCase):

    def test_generate_uuid4(self):
        u1 = generate_uuid4()
        u2 = generate_uuid4()
        self.assertNotEqual(u1, u2)
        self.assertTrue(is_valid_uuid(u1))
        self.assertTrue(is_valid_uuid(u2))

    def test_generate_uuid5_deterministic(self):
        ns = "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
        u_a1 = generate_uuid5(ns, "test-resource")
        u_a2 = generate_uuid5(ns, "test-resource")
        u_b = generate_uuid5(ns, "different-resource")
        self.assertEqual(u_a1, u_a2)
        self.assertNotEqual(u_a1, u_b)
        self.assertTrue(is_valid_uuid(u_a1))

    def test_is_valid_uuid(self):
        self.assertTrue(is_valid_uuid("c9a646d3-9c61-4cd7-893e-3f47287e0123"))
        self.assertFalse(is_valid_uuid("invalid-uuid-string"))
        self.assertFalse(is_valid_uuid(""))
        self.assertFalse(is_valid_uuid(None))

    def test_short_uuid_roundtrip(self):
        canonical = generate_uuid4()
        compact = short_uuid(canonical)
        self.assertEqual(len(compact), 22)
        recovered = expand_short_uuid(compact)
        self.assertEqual(recovered, canonical)

    def test_random_short_uuid(self):
        compact = short_uuid()
        self.assertEqual(len(compact), 22)
        expanded = expand_short_uuid(compact)
        self.assertTrue(is_valid_uuid(expanded))


if __name__ == "__main__":
    unittest.main()
