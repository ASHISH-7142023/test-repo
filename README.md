# DevToolkit - General Purpose Utility Library

[![DevToolkit CI](https://github.com/ASHISH-7142023/test-repo/actions/workflows/test.yml/badge.svg)](https://github.com/ASHISH-7142023/test-repo/actions)
![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Tests](https://img.shields.io/badge/tests-330%2B%20passed-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A lightweight, zero-dependency developer utility toolkit for daily software engineering tasks. Includes 110+ robust, battle-tested modules for text processing, date calculations, file operations, caching, rate limiting, cryptographic tokens, encoding, collections, system metrics, security hashing, networking, event buses, resilience, pagination, semver, algorithms, graph theory, tries, geometric vectors, Fenwick trees, segment trees, A*, Huffman coding, and data structures.

---

## 📦 Modules & Capabilities

| Module | Purpose | Key Functions / Classes |
|---|---|---|
| **`bloom_filter_scalable.py`** | Scalable Bloom Filter | `ScalableBloomFilter` (`add`, `contains`, `num_filters`) |
| **`lfu_cache.py`** | O(1) Least Frequently Used cache | `LFUCache` (`get`, `put`, `delete`, `clear`) |
| **`treap.py`** | Cartesian tree / BST + heap | `Treap` (`insert`, `search`, `remove`, `kth_smallest`) |
| **`levenshtein_automaton.py`** | Automaton fuzzy dictionary search | `LevenshteinAutomaton`, `fuzzy_search` |
| **`kd_tree.py`** | k-d spatial tree & range box | `KDTree` (`nearest_neighbor`, `range_query`) |
| **`bellman_ford.py`** | Arbitrary weight shortest path | `bellman_ford`, `shortest_path_bf` |
| **`bipartite_matching.py`** | Hopcroft-Karp maximum matching | `hopcroft_karp` |
| **`min_spanning_tree.py`** | Kruskal & Prim MST algorithms | `kruskal_mst`, `prim_mst` |
| **`base62_utils.py`** | Base62 alphanumeric compacting | `base62_encode_int`, `base62_decode_int` |
| **`hilbert_curve.py`** | 2D Hilbert space-filling curve | `point_to_hilbert`, `hilbert_to_point` |
| **`totp_utils.py`** | RFC 6238 TOTP & RFC 4226 HOTP | `totp`, `verify_totp`, `hotp` |
| **`cron_parser.py`** | Cron parser & natural explainer | `explain_cron`, `matches_cron`, `parse_cron` |
| **`json_pointer.py`** | RFC 6901 JSON pointer mutator | `resolve_json_pointer`, `set_json_pointer` |
| **`isbn_utils.py`** | ISBN-10/13 validator & convert | `validate_isbn10`, `validate_isbn13`, `isbn10_to_isbn13` |
| **`bloom_filter_counting.py`** | Counting Bloom Filter | `CountingBloomFilter` (`add`, `remove`, `contains`, `count`) |
| **`suffix_array.py`** | Suffix Array & substring search | `build_suffix_array`, `suffix_array_search`, `longest_repeated_substring` |
| **`tarjan_scc.py`** | Strongly connected components | `TarjanSCC` (`add_edge`, `find_sccs`) |
| **`astar_search.py`** | 2D Grid A* pathfinding | `astar_grid`, `manhattan_distance`, `euclidean_distance` |
| **`fenwick_tree.py`** | Binary Indexed Tree (BIT) | `FenwickTree` (`update`, `prefix_sum`, `range_sum`) |
| **`segment_tree.py`** | Segment tree range queries | `SegmentTree` (`query`, `update`) |
| **`radix_sort.py`** | Linear time integer sort | `radix_sort_integers`, `counting_sort` |
| **`topological_kahns.py`** | Kahn DAG topological sort | `kahns_topological_sort` |
| **`rabin_karp.py`** | Rolling hash substring search | `rabin_karp_search`, `rabin_karp_contains` |
| **`huffman_coding.py`** | Huffman compression & prefix codes | `huffman_encode`, `huffman_decode`, `build_huffman_tree` |
| **`morse_code.py`** | International Morse code | `text_to_morse`, `morse_to_text` |
| **`roman_numerals.py`** | Roman numeral converter | `to_roman`, `from_roman` |
| **`natural_sort.py`** | Human alphanumeric natural sort | `natural_sort`, `natural_sort_key` |
| **`crc32_utils.py`** | IEEE 802.3 CRC32 checksum | `crc32_compute`, `crc32_hex` |
| **`color_cmyk.py`** | CMYK color space conversions | `rgb_to_cmyk`, `cmyk_to_rgb` |
| **`geo_geohash.py`** | Geohash coordinate encoder | `encode_geohash`, `decode_geohash` |
| **`units_converter.py`** | Metric & imperial unit conversions | `convert_length`, `convert_weight`, `convert_temperature`, `convert_bytes` |
| **`diffie_hellman.py`** | Key exchange simulation | `DiffieHellmanParty` (`get_public_key`, `compute_shared_secret`) |
| **`semver_range.py`** | SemVer range expression matcher | `satisfies_range` (`^`, `~`, `>=`, `<=`) |
| **`expression_evaluator.py`**| Shunting-Yard RPN math evaluator | `evaluate_expression`, `shunting_yard`, `evaluate_rpn` |
| **`ring_buffer.py`** | Circular ring buffer | `CircularBuffer` (`append`, `popleft`, `peek`, `overwrite`) |
| **`skip_list.py`** | Probabilistic indexing O(log n) | `SkipList` (`insert`, `contains`, `remove`, `to_list`) |
| **`interval_tree.py`** | 1D range queries & overlap | `IntervalTree` (`insert`, `find_overlapping`, `find_at_point`) |
| **`kmp_search.py`** | Knuth-Morris-Pratt string search | `kmp_search`, `kmp_contains`, `compute_lps` |
| **`boyer_moore.py`** | Boyer-Moore string search | `boyer_moore_search`, `boyer_moore_contains` |
| **`dijkstra.py`** | Shortest path graph algorithm | `WeightedGraph` (`add_edge`, `dijkstra`, `shortest_path`) |
| **`mime_utils.py`** | MIME type and extension inference | `guess_mime_type`, `guess_extension`, `is_text_mime`, `is_image_mime` |
| **`base58_utils.py`** | Base58 encoding & checksums | `b58encode`, `b58decode`, `b58encode_check`, `b58decode_check` |
| **`base32_utils.py`** | RFC 4648 Base32 encoding | `base32_encode`, `base32_decode` |
| **`fraction_utils.py`**| Rational fraction arithmetic | `RationalFraction`, `approximate_float` |
| **`color_hsl.py`** | HSL color space conversions | `rgb_to_hsl`, `hsl_to_rgb`, `hex_to_hsl`, `hsl_to_hex` |
| **`cron_next.py`** | Next cron run calculator | `get_next_cron_run` |
| **`lru_k_cache.py`** | Scan-resistant LRU-K caching | `LRUKCache` (`get`, `put`, `delete`, `clear`) |
| **`vector3d.py`** | 3D vector geometry & angles | `Vector3D` (`dot`, `cross`, `magnitude`, `normalize`, `angle_with`) |
| **`fuzzy_set.py`** | Fuzzy logic set operations | `TriangularMembership`, `FuzzySet` (`union`, `intersection`, `complement`) |
| **`phonetic_utils.py`**| Soundex phonetic encoding | `soundex`, `soundex_matches` |
| **`convex_hull.py`** | Graham Scan 2D convex hull | `convex_hull_graham`, `polygon_area`, `Point2D` |
| **`tree_serializer.py`**| Bracket & dict tree format | `serialize_to_brackets`, `deserialize_from_brackets`, `tree_to_dict` |
| **`time_window.py`** | Rolling sliding & tumbling windows | `SlidingWindowCounter`, `TumblingWindowAggregator` |
| **`string_utils.py`** | Text manipulation & formatting | `slugify`, `camel_to_snake`, `mask_sensitive`, `strip_html_tags` |
| **`hash_ring.py`** | Consistent hashing & sharding | `HashRing` (`add_node`, `remove_node`, `get_node`) |
| **`stopwatch.py`** | Multi-lap split timing | `SplitStopwatch` (`start`, `lap`, `stop`, `summary`) |
| **`bit_utils.py`** | Bitwise manipulation | `count_set_bits`, `is_power_of_two`, `get_bit`, `set_bit` |
| **`trie_utils.py`** | Prefix tree autocomplete | `Trie` (`insert`, `search`, `autocomplete`) |
| **`disjoint_set.py`** | Union-Find DSU | `DisjointSet` (`find`, `union`, `connected`) |
| **`graph_utils.py`** | Graph topological sort & BFS | `Graph` (`add_edge`, `topological_sort`, `shortest_path_bfs`) |
| **`levenshtein_utils.py`**| Edit distance & fuzzy matching | `levenshtein_distance`, `similarity_ratio`, `find_closest_match` |
| **`binary_search_utils.py`**| Binary search & bounds | `binary_search`, `search_range` |
| **`luhn_utils.py`** | Luhn algorithm validation | `validate_luhn`, `calculate_luhn_digit` |
| **`color_contrast.py`** | WCAG AA/AAA accessibility | `contrast_ratio`, `is_wcag_aa`, `is_wcag_aaa` |
| **`url_builder.py`** | Fluent URL chaining | `URLBuilder` (`set_host`, `add_path`, `add_param`) |
| **`top_k_stream.py`** | Streaming Top-K items | `TopKStream` (`add`, `get_top_k`) |
| **`markdown_builder.py`**| Fluent Markdown document builder | `MarkdownBuilder` (`header`, `bullet_list`, `code_block`) |
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
| **`config_utils.py`** | Environment configuration loader | `load_config_from_env` |
| **`decorator_utils.py`**| Caching & memoization decorators | `memoize`, `timeit` |
| **`diff_utils.py`** | Unified line and word diffs | `generate_line_diff`, `generate_word_diff` |
| **`humanize_utils.py`**| Natural human formatting | `natural_time`, `intcomma`, `ordinal` |
| **`geo_utils.py`** | Haversine distance & geocoding | `haversine_distance`, `bounding_box` |
| **`regex_patterns.py`**| Precompiled regular expressions | `extract_emails`, `extract_urls`, `extract_ipv4` |
| **`serializer_utils.py`**| Safe JSON datetime encoder | `safe_json_dumps`, `safe_json_loads` |
| **`date_utils.py`** | Date difference & human duration | `format_iso`, `human_readable_duration` |
| **`file_utils.py`** | Safe directory & file helpers | `safe_read_text`, `safe_write_text`, `get_file_checksum` |
| **`validators.py`** | Regex and data validators | `is_valid_email`, `is_valid_url`, `is_strong_password` |
| **`math_utils.py`** | Math & geometry calculations | `clamp`, `lerp`, `round_to_nearest`, `percent_change` |
| **`encoding_utils.py`**| Base64 & Hex encoding helpers | `to_base64`, `from_base64`, `to_hex`, `from_hex` |
| **`retry_utils.py`** | Exponential backoff decorator | `retry` |
| **`collection_utils.py`**| Flattening, chunking, groups | `flatten`, `chunk`, `group_by`, `unique` |
| **`crypto_utils.py`** | Tokens & HMAC signatures | `generate_secure_token`, `compute_hmac` |
| **`system_utils.py`** | Platform details & formatting | `get_platform_info`, `get_disk_usage`, `format_bytes` |
| **`env_utils.py`** | Typed env variable retrieval | `get_env_str`, `get_env_int`, `get_env_bool`, `get_env_list` |
| **`color_utils.py`** | ANSI terminal colors | `colorize`, `strip_ansi` |
| **`cache_utils.py`** | In-memory TTL cache | `TTLCache` (`set`, `get`, `delete`, `clean_expired`) |
| **`rate_limiter.py`** | Token Bucket algorithm | `TokenBucketRateLimiter` (`acquire`, `consume`) |
| **`uuid_utils.py`** | UUID generation & validation | `generate_uuid4`, `generate_uuid5`, `is_valid_uuid`, `short_uuid` |
| **`csv_utils.py`** | CSV reader and writer | `read_csv_dicts`, `write_csv_dicts` |
| **`benchmark_utils.py`**| CPU timing & execution bench | `benchmark`, `BenchmarkResult` |
| **`type_defs.py`** | Typing protocols & base models | `Serializable`, `DictSerializable`, `BaseModel` |
| **`logger_utils.py`** | Structured JSON & console logs | `DevLogger`, `LogLevel` |

---

## 🚀 Quick Start

```python
from src.expression_evaluator import evaluate_expression
from src.morse_code import text_to_morse, morse_to_text
from src.roman_numerals import to_roman, from_roman
from src.units_converter import convert_length

# 1. Mathematical Expression Evaluation
print(evaluate_expression("3 + 4 * 2 ^ (1 + 1)")) # 19.0

# 2. International Morse Code
morse = text_to_morse("HELLO WORLD")
print(morse) # .... . .-.. .-.. --- / .-- --- .-. .-.. -..
print(morse_to_text(morse)) # HELLO WORLD

# 3. Roman Numerals
print(to_roman(2026)) # MMXXVI
print(from_roman("MMXXVI")) # 2026

# 4. Units Converter
print(convert_length(5, "mi", "km")) # ~8.046 km
```

---

## 🛠️ CLI Usage

```bash
# Morse Code encoding and decoding
python cli.py morse-encode "HELLO WORLD"
python cli.py morse-decode ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

# Roman Numeral conversion
python cli.py to-roman 2026
python cli.py from-roman MMXXVI

# Unit conversions
python cli.py convert-units 10 km mi

# CMYK color conversion
python cli.py rgb-to-cmyk 255 128 0

# Base58 encode / decode
python cli.py b58-encode "Hello World!"

# Soundex phonetics
python cli.py soundex "Robert"
```

---

## 🧪 Testing

Execute the comprehensive test suite with zero external dependencies:

```bash
python -m unittest discover tests -v
```

All 280+ unit tests execute in under 7 seconds!

---

## 📄 License

MIT © 2026 DevToolkit Contributors
