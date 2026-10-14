"""Unit tests for DevLogger structured and colored outputs."""

import json
import unittest
from src.logger_utils import DevLogger, LogLevel


class TestLoggerUtils(unittest.TestCase):

    def test_level_filtering(self):
        logger = DevLogger(name="test", level=LogLevel.WARN)
        self.assertIsNone(logger.debug("Debug msg"))
        self.assertIsNone(logger.info("Info msg"))
        self.assertIsNotNone(logger.warn("Warn msg"))
        self.assertIsNotNone(logger.error("Error msg"))

    def test_json_formatting(self):
        logger = DevLogger(name="service", level=LogLevel.INFO, json_format=True)
        raw_json = logger.info("User logged in", user_id="u123", ip="127.0.0.1")
        self.assertIsNotNone(raw_json)
        data = json.loads(raw_json)
        self.assertEqual(data["name"], "service")
        self.assertEqual(data["level"], "INFO")
        self.assertEqual(data["message"], "User logged in")
        self.assertEqual(data["user_id"], "u123")
        self.assertEqual(data["ip"], "127.0.0.1")

    def test_console_formatting(self):
        logger = DevLogger(name="cli", level=LogLevel.INFO, json_format=False)
        output = logger.info("Task completed")
        self.assertIn("cli: Task completed", output)
        self.assertIn("[INFO]", output)


if __name__ == "__main__":
    unittest.main()
