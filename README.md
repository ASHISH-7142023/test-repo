# DevToolkit - General Purpose Utility Library

[![DevToolkit CI](https://github.com/ASHISH-7142023/test-repo/actions/workflows/test.yml/badge.svg)](https://github.com/ASHISH-7142023/test-repo/actions)
![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Tests](https://img.shields.io/badge/tests-150%2B%20passed-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A lightweight, zero-dependency developer utility toolkit for daily software engineering tasks. Includes 45+ robust, battle-tested modules for text processing, date calculations, file operations, caching, rate limiting, cryptographic tokens, encoding, collections, system metrics, security hashing, networking, event buses, resilience, pagination, semver, and algorithms.

---

## 📦 Modules & Capabilities

| Module | Purpose | Key Functions |
|---|---|---|
| **`string_utils.py`** | Text manipulation & formatting | `slugify`, `camel_to_snake`, `mask_sensitive`, `strip_html_tags` |
| **`pagination_utils.py`**| Slicing and cursor pagination | `paginate_list`, `cursor_paginate`, `Page` |
| **`jwt_utils.py`** | HS256 JSON Web Tokens | `encode_jwt`, `decode_jwt` |
| **`query_utils.py`** | URL query parameters | `parse_query_params`, `build_query_string`, `filter_query_params` |
| **`tree_utils.py`** | Hierarchical data & traversal | `TreeNode`, `dfs_traverse`, `bfs_traverse`, `find_node` |
| **`semver_utils.py`** | Semantic versioning 2.0.0 | `parse_semver`, `compare_semver`, `bump_semver` |
| **`table_utils.py`** | ASCII and Markdown tables | `format_ascii_table`, `format_markdown_table` |
| **`matrix_utils.py`** | 2D matrix transformations | `transpose`, `rotate_90_clockwise`, `matrix_multiply` |
| **`random_utils.py`** | Weighted random sampling | `weighted_choice`, `random_alphanumeric`, `roll_dice` |
| **`cron_utils.py`** | Cron expression parser | `parse_cron_field`, `matches_cron` |
| **`currency_utils.py`**| Multi-currency formatting | `format_currency`, `is_valid_currency_code` |
| **`bloom_filter.py`** | Probabilistic membership | `BloomFilter` (`add`, `contains`) |
| **`circuit_breaker.py`**| Fault tolerance & trips | `CircuitBreaker` (`CLOSED`, `OPEN`, `HALF_OPEN`) |
| **`fsm_utils.py`** | Finite state machine | `StateMachine` (`add_transition`, `trigger`) |
| **`slug_enhancements.py`**| Stop-word slugifier | `advanced_slugify` |
| **`template_utils.py`**| Mustache template engine | `render_template` |
| **`priority_queue.py`**| Thread-safe min/max heap | `PriorityQueue` (`push`, `pop`, `peek`) |
| **`security_utils.py`**| PBKDF2-HMAC password hashing | `hash_password`, `verify_password`, `generate_salt` |
| **`net_utils.py`** | IP and subnet verification | `is_valid_ipv4`, `is_valid_ipv6`, `is_private_ip`, `ip_in_cidr` |
| **`stats_utils.py`** | Descriptive statistics | `median`, `percentile`, `interquartile_range`, `z_scores` |
| **`event_bus.py`** | Pub-sub event broker | `EventBus` (`subscribe`, `publish`, `unsubscribe`, `clear`) |
| **`async_utils.py`** | Async concurrency control | `gather_with_concurrency`, `batch_process` |
| **`diff_utils.py`** | Object and text unified diffs | `diff_dicts`, `unified_diff_text` |
| **`humanize_utils.py`**| Natural formatting | `ordinal`, `intcomma`, `natural_list` |
| **`geo_utils.py`** | Coordinates & Haversine distance | `haversine_distance_km`, `calculate_bearing`, `is_valid_coordinates` |
| **`regex_patterns.py`**| Pattern entity extractors | `extract_emails`, `extract_urls`, `extract_hashtags`, `extract_mentions` |
| **`serializer_utils.py`**| Enhanced JSON encoder | `DevToolkitJSONEncoder`, `to_json`, `from_json` |
| **`logger_utils.py`** | Structured & color logger | `DevLogger` (`debug`, `info`, `warn`, `error`) |
| **`decorator_utils.py`**| Functional decorators | `memoize`, `deprecated`, `once` |
| **`config_utils.py`** | INI & Key-Value parsers | `parse_ini_string`, `parse_key_value_string`, `serialize_ini` |
| **`type_defs.py`** | Typing protocols & aliases | `JSONType`, `Number`, `Serializable`, `Deserializable` |
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

# Bump semantic versions
python cli.py semver-bump 1.2.3 --type minor

# Format currencies
python cli.py currency 1500 --code USD

# Hash and verify passwords with PBKDF2
python cli.py hash-password "MySecretPassword"
python cli.py verify-password "MySecretPassword" "$pbkdf2-sha256$10000$..."

# Format numbers with ordinals and commas
python cli.py ordinal 42
python cli.py intcomma 1000000

# Inspect IP address status
python cli.py ip-info "192.168.1.1"

# Generate canonical or short 22-char UUID
python cli.py uuid
python cli.py uuid --short

# System diagnostics and disk space
python cli.py sys-info
python cli.py disk-usage
```

---

## 🧪 Running the Automated Test Suite

DevToolkit comes with a comprehensive suite of 150+ unit tests:

```bash
python -m unittest discover tests -v
```

---

## 📄 License
MIT License. Built for modularity, clean architecture, and developer productivity.
