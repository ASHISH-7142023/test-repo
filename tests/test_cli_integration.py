"""Integration tests executing DevToolkit CLI commands."""

import subprocess
import sys
import unittest


class TestCLIIntegration(unittest.TestCase):

    def run_cli(self, *args):
        cmd = [sys.executable, "cli.py"] + list(args)
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return res.returncode, res.stdout.strip(), res.stderr.strip()

    def test_cli_slug(self):
        code, out, _ = self.run_cli("slug", "Hello World 2026")
        self.assertEqual(code, 0)
        self.assertEqual(out, "hello-world-2026")

    def test_cli_uuid(self):
        code, out, _ = self.run_cli("uuid")
        self.assertEqual(code, 0)
        self.assertEqual(len(out), 36)

    def test_cli_ordinal(self):
        code, out, _ = self.run_cli("ordinal", "42")
        self.assertEqual(code, 0)
        self.assertEqual(out, "42nd")

    def test_cli_intcomma(self):
        code, out, _ = self.run_cli("intcomma", "1000000")
        self.assertEqual(code, 0)
        self.assertEqual(out, "1,000,000")


if __name__ == "__main__":
    unittest.main()
