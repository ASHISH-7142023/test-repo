"""Unit tests for CSV processing utilities."""

import unittest
from src.csv_utils import detect_delimiter, read_csv_dicts, write_csv_dicts


class TestCsvUtils(unittest.TestCase):

    def test_detect_delimiter(self):
        comma_data = "name,age,city\nAlice,30,NYC\nBob,25,SF"
        tab_data = "name\tage\tcity\nAlice\t30\tNYC"
        pipe_data = "name|age|city\nAlice|30|NYC"
        self.assertEqual(detect_delimiter(comma_data), ",")
        self.assertEqual(detect_delimiter(tab_data), "\t")
        self.assertEqual(detect_delimiter(pipe_data), "|")

    def test_read_csv_dicts(self):
        csv_text = "id,username,role\n1,admin,superadmin\n2,john,editor"
        rows = read_csv_dicts(csv_text)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0], {"id": "1", "username": "admin", "role": "superadmin"})
        self.assertEqual(rows[1], {"id": "2", "username": "john", "role": "editor"})

    def test_write_csv_dicts(self):
        rows = [
            {"product": "Apples", "qty": 10},
            {"product": "Oranges", "qty": 25}
        ]
        csv_out = write_csv_dicts(rows)
        self.assertIn("product,qty\n", csv_out)
        self.assertIn("Apples,10\n", csv_out)
        self.assertIn("Oranges,25\n", csv_out)

    def test_empty_cases(self):
        self.assertEqual(read_csv_dicts(""), [])
        self.assertEqual(write_csv_dicts([]), "")


if __name__ == "__main__":
    unittest.main()
