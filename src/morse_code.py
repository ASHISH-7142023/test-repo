"""International Morse Code encoder and decoder."""

MORSE_TABLE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "0": "-----", ".": ".-.-.-", ",": "--..--", "?": "..--..",
}

REVERSE_MORSE = {v: k for k, v in MORSE_TABLE.items()}


def text_to_morse(text: str) -> str:
    """Convert text into Morse code representation."""
    words = text.strip().upper().split()
    encoded_words = []
    for word in words:
        letters = [MORSE_TABLE[ch] for ch in word if ch in MORSE_TABLE]
        if letters:
            encoded_words.append(" ".join(letters))
    return " / ".join(encoded_words)


def morse_to_text(morse: str) -> str:
    """Convert Morse code back into plain text string."""
    words = morse.strip().split(" / ")
    decoded_words = []
    for word in words:
        letters = [REVERSE_MORSE.get(code, "") for code in word.split() if code in REVERSE_MORSE]
        decoded_words.append("".join(letters))
    return " ".join(decoded_words)
