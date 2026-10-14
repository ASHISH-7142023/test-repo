"""Unit tests for enhanced JSON serializer and custom encoders."""

import json
import uuid
import unittest
from datetime import datetime
from src.serializer_utils import to_json, from_json


class TestSerializerUtils(unittest.TestCase):

    def test_serialize_datetime_and_uuid(self):
        now = datetime(2026, 10, 14, 12, 0, 0)
        uid = uuid.UUID("12345678-1234-5678-1234-567812345678")
        data = {
            "created_at": now,
            "id": uid,
            "tags": {"admin", "developer"}
        }
        res = to_json(data)
        parsed = from_json(res)

        self.assertEqual(parsed["created_at"], "2026-10-14T12:00:00")
        self.assertEqual(parsed["id"], "12345678-1234-5678-1234-567812345678")
        self.assertCountEqual(parsed["tags"], ["admin", "developer"])


if __name__ == "__main__":
    unittest.main()
