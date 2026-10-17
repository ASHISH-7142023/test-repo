import unittest
from src.mime_utils import guess_mime_type, guess_extension, is_text_mime, is_image_mime

class TestMimeUtils(unittest.TestCase):
    def test_guess_mime(self):
        self.assertEqual(guess_mime_type("index.html"), "text/html")
        self.assertEqual(guess_mime_type("/path/to/data.json"), "application/json")
        self.assertEqual(guess_mime_type("photo.JPEG"), "image/jpeg")
        self.assertEqual(guess_mime_type(".css"), "text/css")
        self.assertEqual(guess_mime_type("unknown.xyz"), "application/octet-stream")

    def test_guess_extension(self):
        self.assertEqual(guess_extension("text/html"), ".html")
        self.assertEqual(guess_extension("image/png"), ".png")
        self.assertIsNone(guess_extension("application/unknown-binary"))

    def test_categories(self):
        self.assertTrue(is_text_mime("text/plain"))
        self.assertTrue(is_text_mime("application/json"))
        self.assertFalse(is_text_mime("image/png"))
        self.assertTrue(is_image_mime("image/webp"))
        self.assertFalse(is_image_mime("application/pdf"))

if __name__ == "__main__":
    unittest.main()
