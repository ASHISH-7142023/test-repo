"""Integration tests for extended CLI commands."""

import subprocess
import sys
import unittest


class TestCLIExtended(unittest.TestCase):

    def run_cli(self, *args):
        cmd = [sys.executable, "cli.py"] + list(args)
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return res.returncode, res.stdout.strip(), res.stderr.strip()

    def test_cli_semver_bump(self):
        code, out, _ = self.run_cli("semver-bump", "1.0.0", "--type", "minor")
        self.assertEqual(code, 0)
        self.assertEqual(out, "1.1.0")

    def test_cli_currency(self):
        code, out, _ = self.run_cli("currency", "1500", "--code", "USD")
        self.assertEqual(code, 0)
        self.assertEqual(out, "$1,500.00")


if __name__ == "__main__":
    unittest.main()
