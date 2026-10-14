"""Unit tests for custom type definitions and runtime protocols."""

import unittest
from src.type_defs import Serializable, Deserializable, JSONType, Number


class MockDataModel:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def to_dict(self):
        return {"name": self.name, "value": self.value}

    @classmethod
    def from_dict(cls, data):
        return cls(name=data["name"], value=data["value"])


class MockNonSerializable:
    pass


class TestTypeDefs(unittest.TestCase):

    def test_serializable_protocol_runtime_check(self):
        model = MockDataModel("sample", 42)
        self.assertIsInstance(model, Serializable)
        self.assertIsInstance(model, Deserializable)

    def test_non_serializable_protocol_runtime_check(self):
        non_model = MockNonSerializable()
        self.assertNotIsInstance(non_model, Serializable)
        self.assertNotIsInstance(non_model, Deserializable)

    def test_model_serialization_methods(self):
        m = MockDataModel("test", 100)
        d = m.to_dict()
        self.assertEqual(d, {"name": "test", "value": 100})
        m2 = MockDataModel.from_dict(d)
        self.assertEqual(m2.name, "test")
        self.assertEqual(m2.value, 100)


if __name__ == "__main__":
    unittest.main()
