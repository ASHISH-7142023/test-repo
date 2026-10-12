# DevToolkit - General Purpose Utility Library

[![DevToolkit CI](https://github.com/ASHISH-7142023/test-repo/actions/workflows/test.yml/badge.svg)](https://github.com/ASHISH-7142023/test-repo/actions)
![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Tests](https://img.shields.io/badge/tests-33%20passed-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A lightweight, zero-dependency utility toolkit for daily software engineering tasks. Includes robust, battle-tested modules for text processing, date calculations, file operations, cryptographic tokens, encoding, collections, and resilience.

---

## 📦 Modules & Capabilities

### 1. String Utilities (`src/string_utils.py`)
- **`slugify(text)`**: Creates URL-safe ASCII slugs from arbitrary strings.
- **`camel_to_snake(text)`** & **`snake_to_camel(text)`**: Seamless case conversions.
- **`truncate_words(text, max_words=10)`**: Word-level text truncation with custom ellipsis.
- **`mask_sensitive(text, visible_chars=4)`**: Masks tokens, API keys, and account identifiers.
- **`strip_html_tags(html)`**: Strips HTML tags from formatted text.

### 2. DateTime Helpers (`src/date_utils.py`)
- **`format_iso(dt)`**: Standardized ISO 8601 UTC timestamp formatting.
- **`human_readable_duration(seconds)`**: Converts raw seconds to readable intervals (`2d 4h`, `15m 30s`).
- **`days_between(date1, date2)`**: Date difference calculation.
- **`is_leap_year(year)`**: Accurate leap year detection.

### 3. File System & I/O (`src/file_utils.py`)
- **`atomic_write_text(file_path, content)`**: Atomically writes files using temp files to prevent corruption.
- **`safe_read_json(file_path, default)`**: Reads JSON with safe fallbacks on errors.
- **`get_file_checksum(file_path)`**: Computes streaming SHA256 checksums.

### 4. Encoding & Representation (`src/encoding_utils.py`)
- **`to_base64(text, url_safe=False)`** & **`from_base64(encoded)`**: Standard and URL-safe Base64.
- **`to_hex(text)`** & **`from_hex(hex_str)`**: Hexadecimal string encoders.
- **`url_encode(text)`** & **`url_decode(text)`**: Query parameter encoding.

### 5. Collections & Dictionaries (`src/collection_utils.py`)
- **`chunk_list(items, chunk_size)`**: Splits lists into smaller batches.
- **`dedupe(items)`**: Preserves order while filtering duplicates.
- **`flatten_dict(nested_dict)`**: Flattens nested maps into dot-notated keys.
- **`deep_merge(dict1, dict2)`**: Recursively merges multiple dictionaries.

### 6. Cryptography & Security (`src/crypto_utils.py`)
- **`generate_secure_token(nbytes=32)`**: Cryptographically strong random URL tokens.
- **`hash_sha256(text)`**: Fast SHA-256 string hashing.
- **`constant_time_compare(val1, val2)`**: Constant-time timing-attack safe comparison.

### 7. Resilience & Retries (`src/retry_utils.py`)
- **`@retry(max_attempts=3, delay=0.1, backoff=2.0)`**: Exponential backoff decorator for network operations.

### 8. System Diagnostics (`src/system_utils.py`)
- **`get_platform_info()`**: Operating system, architecture, and Python runtime info.
- **`get_disk_usage(path)`**: Storage capacity, used space, and free space formatting.
- **`format_bytes(bytes_count)`**: Converts raw bytes to `KB`, `MB`, `GB`, `TB`.

### 9. Validation & Math (`src/validators.py`, `src/math_utils.py`)
- Email, URL, strong password complexity, moving averages, percent change, and clamping.

---

## 💻 CLI Usage

DevToolkit includes an interactive command-line interface:

```bash
# Generate a clean slug
python cli.py slug "Building Scalable Architecture in 2026"

# Generate a cryptographically secure token
python cli.py token --bytes 32

# Encode and decode Base64
python cli.py b64-encode "Hello World"
python cli.py b64-decode "SGVsbG8gV29ybGQ="

# Calculate SHA256 checksum of a file
python cli.py checksum README.md

# Format seconds into duration
python cli.py duration 86450
```

---

## 🧪 Running the Automated Test Suite

DevToolkit comes with a comprehensive suite of 33 unit tests:

```bash
python -m unittest discover tests -v
```

---

## 📄 License
MIT License. Built for modularity, clean architecture, and developer productivity.
