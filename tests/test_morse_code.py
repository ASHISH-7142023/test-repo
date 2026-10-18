import unittest
from src.morse_code import text_to_morse, morse_to_text

class TestMorseCode(unittest.TestCase):
    def test_sos(self):
        self.assertEqual(text_to_morse("SOS"), "... --- ...")
        self.assertEqual(morse_to_text("... --- ..."), "SOS")

    def test_words(self):
        text = "HELLO WORLD"
        morse = text_to_morse(text)
        self.assertEqual(morse_to_text(morse), text)

if __name__ == "__main__":
    unittest.main()
