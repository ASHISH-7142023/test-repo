# DevToolkit - General Purpose Utility Library

[![DevToolkit CI](https://github.com/ASHISH-7142023/test-repo/actions/workflows/test.yml/badge.svg)](https://github.com/ASHISH-7142023/test-repo/actions)
![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A lightweight, zero-dependency utility toolkit for daily software engineering tasks. Includes robust modules for text manipulation, date formatting, data validation, and mathematics.

---

## 📦 Modules & Capabilities

### 1. String Utilities (`src/string_utils.py`)
- **`slugify(text)`**: Creates URL-safe ASCII slugs from arbitrary strings.
- **`camel_to_snake(text)`** & **`snake_to_camel(text)`**: Seamless case conversions.
- **`truncate_words(text, max_words=10)`**: Word-level text truncation with custom ellipsis.
- **`mask_sensitive(text, visible_chars=4)`**: Masks tokens, API keys, and account identifiers.

```python
from src.string_utils import slugify, mask_sensitive

slug = slugify("Hello World & Special Characters!")
# Output: "hello-world-special-characters"

masked = mask_sensitive("sk_live_9837492817293", visible_chars=4)
# Output: "*****************7293"
```

### 2. DateTime Helpers (`src/date_utils.py`)
- **`format_iso(dt)`**: Standardized ISO 8601 UTC timestamp formatting.
- **`human_readable_duration(seconds)`**: Converts raw seconds to readable intervals (`2d 4h`, `15m 30s`).
- **`days_between(date1, date2)`**: Date difference calculation.
- **`is_leap_year(year)`**: Accurate leap year detection.

### 3. Data & Credential Validators (`src/validators.py`)
- **`is_valid_email(email)`**: RFC-compliant email structure verification.
- **`is_valid_url(url)`**: HTTP/HTTPS URL validation.
- **`is_strong_password(password)`**: Password complexity audits (length, casing, digits, symbols).
- **`validate_required_keys(data, required_keys)`**: JSON/dict payload integrity checks.

### 4. Math & Statistics (`src/math_utils.py`)
- **`clamp(val, min_val, max_val)`**: Bounds numeric values within a range.
- **`percent_change(initial, final)`**: Computes percentage change.
- **`moving_average(data, window_size)`**: Sliding window moving averages.
- **`standard_deviation(data)`**: Sample and population standard deviations.

---

## 💻 CLI Usage

DevToolkit includes an interactive command-line interface:

```bash
# Generate a clean slug
python cli.py slug "Building Scalable Architecture in 2026"

# Mask a secret API token
python cli.py mask "ghp_1234567890abcdef" --visible 4

# Format duration
python cli.py duration 86450

# Validate password complexity
python cli.py validate-password "MyP@ssw0rd2026!"
```

---

## 🧪 Running Tests

DevToolkit comes with a complete test suite:

```bash
python -m unittest discover tests -v
```

---

## 📄 License
MIT License. Built for modularity, clean architecture, and developer productivity.
