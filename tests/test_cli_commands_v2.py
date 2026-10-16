"""Integration tests for Luhn and contrast CLI commands."""

import subprocess
import sys
import unittest


class TestCLICommandsV2(unittest.TestCase):

    def run_cli(self, *args):
        cmd = [sys.executable, "cli.py"] + list(args)
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return res.returncode, res.stdout.strip(), res.stderr.strip()

    def test_cli_luhn(self):
        code, out, _ = self.run_cli("luhn-check", "49927398716")
        self.assertEqual(code, 0)
        self.assertIn("Luhn Valid: True", out)

    def test_cli_contrast(self):
        code, out, _ = self.run_cli("contrast", "#ffffff", "#000000")
        self.assertEqual(code, 0)
        self.assertIn("Contrast Ratio: 21.0:1", out)


if __name__ == "__main__":
    unittest.main()
