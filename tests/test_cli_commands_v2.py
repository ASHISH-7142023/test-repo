"""Integration tests for extended CLI commands."""

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

    def test_cli_guess_mime(self):
        code, out, _ = self.run_cli("guess-mime", "style.css")
        self.assertEqual(code, 0)
        self.assertEqual(out, "text/css")

    def test_cli_base58_roundtrip(self):
        code, out, _ = self.run_cli("b58-encode", "Hello World!")
        self.assertEqual(code, 0)
        self.assertEqual(out, "2NEpo7TZRRrLZSi2U")

        code2, out2, _ = self.run_cli("b58-decode", "2NEpo7TZRRrLZSi2U")
        self.assertEqual(code2, 0)
        self.assertEqual(out2, "Hello World!")

    def test_cli_soundex(self):
        code, out, _ = self.run_cli("soundex", "Robert")
        self.assertEqual(code, 0)
        self.assertEqual(out, "R163")

        code2, out2, _ = self.run_cli("soundex-match", "Robert", "Rupert")
        self.assertEqual(code2, 0)
        self.assertIn("Soundex Match: True", out2)


if __name__ == "__main__":
    unittest.main()
