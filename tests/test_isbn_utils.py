import unittest
from src.isbn_utils import validate_isbn10, validate_isbn13, isbn10_to_isbn13, format_isbn

class TestISBNUtils(unittest.TestCase):
    def test_valid_isbn10(self):
        self.assertTrue(validate_isbn10("0-306-40615-2"))
        self.assertTrue(validate_isbn10("080442957X"))
        self.assertFalse(validate_isbn10("0804429570"))

    def test_valid_isbn13(self):
        self.assertTrue(validate_isbn13("978-0-306-40615-7"))
        self.assertFalse(validate_isbn13("978-0-306-40615-9"))

    def test_conversion(self):
        isbn13 = isbn10_to_isbn13("0-306-40615-2")
        self.assertEqual(isbn13, "9780306406157")

if __name__ == "__main__":
    unittest.main()
