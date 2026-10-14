"""Unit tests for INI and key-value configuration parsers."""

import unittest
from src.config_utils import parse_ini_string, parse_key_value_string, serialize_ini


class TestConfigUtils(unittest.TestCase):

    def test_parse_ini_string(self):
        ini_content = """
[database]
host = localhost
port = 5432

[server]
debug = true
"""
        config = parse_ini_string(ini_content)
        self.assertIn("database", config)
        self.assertEqual(config["database"]["host"], "localhost")
        self.assertEqual(config["database"]["port"], "5432")
        self.assertEqual(config["server"]["debug"], "true")

    def test_parse_key_value_string(self):
        env_content = """
# App Environment Config
APP_NAME="DevToolkit"
PORT=8080
DEBUG=false
"""
        parsed = parse_key_value_string(env_content)
        self.assertEqual(parsed["APP_NAME"], "DevToolkit")
        self.assertEqual(parsed["PORT"], "8080")
        self.assertEqual(parsed["DEBUG"], "false")

    def test_serialize_ini(self):
        data = {
            "web": {"host": "0.0.0.0", "workers": 4}
        }
        res = serialize_ini(data)
        self.assertIn("[web]", res)
        self.assertIn("host = 0.0.0.0", res)
        self.assertIn("workers = 4", res)


if __name__ == "__main__":
    unittest.main()
