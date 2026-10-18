"""Huffman coding prefix tree compression and decompression."""

import heapq
from collections import Counter
from typing import Dict, Optional, Tuple


class HuffmanNode:
    def __init__(self, char: Optional[str], freq: int):
        self.char = char
        self.freq = freq
        self.left: Optional["HuffmanNode"] = None
        self.right: Optional["HuffmanNode"] = None

    def __lt__(self, other: "HuffmanNode") -> bool:
        return self.freq < other.freq


def build_huffman_tree(text: str) -> Optional[HuffmanNode]:
    """Construct min-heap Huffman tree from character frequencies."""
    if not text:
        return None
    counts = Counter(text)
    pq = [HuffmanNode(char, freq) for char, freq in counts.items()]
    heapq.heapify(pq)

    if len(pq) == 1:
        root = HuffmanNode(None, pq[0].freq)
        root.left = pq[0]
        return root

    while len(pq) > 1:
        n1 = heapq.heappop(pq)
        n2 = heapq.heappop(pq)
        merged = HuffmanNode(None, n1.freq + n2.freq)
        merged.left = n1
        merged.right = n2
        heapq.heappush(pq, merged)

    return pq[0]


def _build_codes(node: Optional[HuffmanNode], prefix: str, codes: Dict[str, str]) -> None:
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = prefix or "0"
        return
    _build_codes(node.left, prefix + "0", codes)
    _build_codes(node.right, prefix + "1", codes)


def huffman_encode(text: str) -> Tuple[str, Dict[str, str]]:
    """Encode text into bit string using Huffman codes."""
    if not text:
        return "", {}
    root = build_huffman_tree(text)
    codes: Dict[str, str] = {}
    _build_codes(root, "", codes)
    encoded = "".join(codes[ch] for ch in text)
    return encoded, codes


def huffman_decode(encoded_bits: str, codes: Dict[str, str]) -> str:
    """Decode bit string back to original characters using code map."""
    if not encoded_bits or not codes:
        return ""
    reverse_map = {v: k for k, v in codes.items()}
    curr = ""
    result = []
    for bit in encoded_bits:
        curr += bit
        if curr in reverse_map:
            result.append(reverse_map[curr])
            curr = ""
    return "".join(result)
