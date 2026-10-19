import unittest
import subprocess
import sys

class TestCLICommandsV4(unittest.TestCase):
    def run_cli(self, args):
        return subprocess.run(
            [sys.executable, "cli.py"] + args,
            capture_output=True,
            text=True
        )

    def test_b62_cli(self):
        res = self.run_cli(["b62-encode", "12345"])
        self.assertEqual(res.returncode, 0)
        code = res.stdout.strip()
        res_dec = self.run_cli(["b62-decode", code])
        self.assertEqual(res_dec.returncode, 0)
        self.assertEqual(res_dec.stdout.strip(), "12345")

    def test_cron_explain_cli(self):
        res = self.run_cli(["cron-explain", "*/15 * * * *"])
        self.assertEqual(res.returncode, 0)
        self.assertIn("Every 15 minutes", res.stdout)

    def test_isbn_cli(self):
        res = self.run_cli(["isbn-validate", "0-306-40615-2"])
        self.assertEqual(res.returncode, 0)
        self.assertIn("Valid ISBN-10", res.stdout)

if __name__ == "__main__":
    unittest.main()
