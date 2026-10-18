"""Integration tests for morse, roman, units, and cmyk CLI subcommands."""

import subprocess
import sys
import unittest


class TestCLICommandsV3(unittest.TestCase):

    def run_cli(self, *args):
        cmd = [sys.executable, "cli.py"] + list(args)
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return res.returncode, res.stdout.strip(), res.stderr.strip()

    def test_cli_morse_roundtrip(self):
        code, out, _ = self.run_cli("morse-encode", "SOS")
        self.assertEqual(code, 0)
        self.assertEqual(out, "... --- ...")

        code2, out2, _ = self.run_cli("morse-decode", "... --- ...")
        self.assertEqual(code2, 0)
        self.assertEqual(out2, "SOS")

    def test_cli_roman_roundtrip(self):
        code, out, _ = self.run_cli("to-roman", "2026")
        self.assertEqual(code, 0)
        self.assertEqual(out, "MMXXVI")

        code2, out2, _ = self.run_cli("from-roman", "MMXXVI")
        self.assertEqual(code2, 0)
        self.assertEqual(out2, "2026")

    def test_cli_convert_units(self):
        code, out, _ = self.run_cli("convert-units", "1", "km", "m")
        self.assertEqual(code, 0)
        self.assertEqual(float(out), 1000.0)

    def test_cli_rgb_to_cmyk(self):
        code, out, _ = self.run_cli("rgb-to-cmyk", "255", "0", "0")
        self.assertEqual(code, 0)
        self.assertIn("C: 0.0%, M: 100.0%, Y: 100.0%, K: 0.0%", out)


if __name__ == "__main__":
    unittest.main()
