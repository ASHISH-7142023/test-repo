# DevToolkit - General Purpose Utility Library

[![DevToolkit CI](https://github.com/ASHISH-7142023/test-repo/actions/workflows/test.yml/badge.svg)](https://github.com/ASHISH-7142023/test-repo/actions)
![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Tests](https://img.shields.io/badge/tests-64%20passed-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A lightweight, zero-dependency developer utility toolkit for daily software engineering tasks. Includes robust, battle-tested modules for text processing, date calculations, file operations, caching, rate limiting, cryptographic tokens, encoding, collections, system metrics, and resilience.

---

## 📦 Modules & Capabilities

| Module | Purpose | Key Functions |
|---|---|---|
| **`string_utils.py`** | Text manipulation & formatting | `slugify`, `camel_to_snake`, `mask_sensitive`, `strip_html_tags` |
| **`date_utils.py`** | Timestamp formatting & intervals | `format_iso`, `human_readable_duration`, `days_between`, `is_leap_year` |
| **`file_utils.py`** | Atomic I/O & file hashing | `atomic_write_text`, `safe_read_json`, `get_file_checksum` |
| **`env_utils.py`** | Environment variable coercion | `get_env_str`, `get_env_bool`, `get_env_int`, `get_env_list`, `require_env` |
| **`color_utils.py`** | ANSI terminal colors & RGB | `colorize`, `rgb`, `hex_color`, `strip_ansi` |
| **`cache_utils.py`** | In-memory thread-safe caching | `TTLCache` (expiration), `LRUCache` (capacity eviction) |
| **`rate_limiter.py`** | Traffic shaping & API limits | `TokenBucketRateLimiter` (`allow`, `acquire`) |
| **`uuid_utils.py`** | UUID generation & compacting | `generate_uuid4`, `generate_uuid5`, `short_uuid`, `expand_short_uuid` |
| **`csv_utils.py`** | Streaming CSV serialization | `detect_delimiter`, `read_csv_dicts`, `write_csv_dicts` |
| **`benchmark_utils.py`** | Execution timing & metrics | `BenchmarkTimer`, `@timed`, `benchmark_function` |
| **`encoding_utils.py`** | Data representation | `to_base64`, `from_base64`, `to_hex`, `from_hex`, `url_encode` |
| **`crypto_utils.py`** | Cryptographic tokens & hashing | `generate_secure_token`, `hash_sha256`, `constant_time_compare` |
| **`collection_utils.py`** | Advanced lists & dict operations | `chunk_list`, `dedupe`, `flatten_dict`, `deep_merge` |
| **`retry_utils.py`** | Network & I/O resilience | `@retry(max_attempts=3, delay=0.1, backoff=2.0)` |
| **`system_utils.py`** | Hardware & OS metrics | `get_platform_info`, `get_disk_usage`, `format_bytes` |
| **`validators.py`** | Format verification | `is_valid_email`, `is_valid_url`, `is_strong_password` |
| **`math_utils.py`** | Statistical helpers | `clamp`, `percent_change`, `moving_average`, `standard_deviation` |

---

## 💻 CLI Usage

DevToolkit includes an interactive command-line interface:

```bash
# Generate a clean URL slug
python cli.py slug "Building Scalable Architecture in 2026"

# Generate canonical or short 22-char UUID
python cli.py uuid
python cli.py uuid --short

# System diagnostics and disk space
python cli.py sys-info
python cli.py disk-usage

# Generate cryptographically secure token
python cli.py token --bytes 32

# Encode and decode Base64
python cli.py b64-encode "Hello World"
python cli.py b64-decode "SGVsbG8gV29ybGQ="

# Calculate SHA256 file checksum
python cli.py checksum README.md

# Format seconds into duration
python cli.py duration 86450
```

---

## 🧪 Running the Automated Test Suite

DevToolkit comes with a comprehensive suite of 64 unit tests:

```bash
python -m unittest discover tests -v
```

---

## 📄 License
MIT License. Built for modularity, clean architecture, and developer productivity.
