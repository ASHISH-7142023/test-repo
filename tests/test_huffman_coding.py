import unittest
from src.huffman_coding import huffman_encode, huffman_decode

class TestHuffmanCoding(unittest.TestCase):
    def test_roundtrip(self):
        text = "this is an example for huffman encoding"
        bits, codes = huffman_encode(text)
        decoded = huffman_decode(bits, codes)
        self.assertEqual(decoded, text)

    def test_single_character(self):
        text = "aaaa"
        bits, codes = huffman_encode(text)
        self.assertEqual(huffman_decode(bits, codes), text)

if __name__ == "__main__":
    unittest.main()
