import unittest
import subprocess
import sys

class TestCLICommandsV5(unittest.TestCase):
    def run_cli(self, args):
        return subprocess.run(
            [sys.executable, "cli.py"] + args,
            capture_output=True,
            text=True
        )

    def test_rle_cli(self):
        res = self.run_cli(["rle-encode", "AAAAABBB"])
        self.assertEqual(res.returncode, 0)
        self.assertEqual(res.stdout.strip(), "5A3B")

    def test_geo_bearing_cli(self):
        res = self.run_cli(["geo-bearing", "0.0", "0.0", "10.0", "0.0"])
        self.assertEqual(res.returncode, 0)
        self.assertIn("0.00°", res.stdout)

if __name__ == "__main__":
    unittest.main()
