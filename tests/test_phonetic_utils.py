import unittest
from src.phonetic_utils import soundex, soundex_matches

class TestPhoneticUtils(unittest.TestCase):
    def test_soundex_values(self):
        self.assertEqual(soundex("Robert"), "R163")
        self.assertEqual(soundex("Rupert"), "R163")
        self.assertEqual(soundex("Washington"), "W252")
        self.assertEqual(soundex("Smith"), "S530")
        self.assertEqual(soundex("Smyth"), "S530")

    def test_soundex_matches(self):
        self.assertTrue(soundex_matches("Robert", "Rupert"))
        self.assertTrue(soundex_matches("Smith", "Smyth"))
        self.assertFalse(soundex_matches("Robert", "Washington"))

if __name__ == "__main__":
    unittest.main()
