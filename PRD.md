# 📋 Product Requirements Document (PRD)

## Project: `DevToolkit`
**Version:** 1.4.0  
**Status:** Active / Production-Ready  
**License:** MIT  
**Target Platform:** Python 3.8+ (Linux, macOS, Windows)

---

## 1. Executive Summary

Modern software engineering frequently suffers from severe **dependency bloat**. Applications often pull in hundreds of transitive dependencies for mundane tasks like rate limiting, phonetic matching, Roman numeral conversions, topological sorting, or calculating great-circle distances. This creates:
1. Significant supply-chain security risks (malicious package takeovers, typosquatting).
2. Dependency version conflicts ("dependency hell").
3. Slow container build times and large disk footprints.

**`DevToolkit`** is a production-grade standard library extension and developer utility toolkit written in **pure Python with zero external dependencies**. It provides over 115+ algorithmic and engineering modules covering advanced computer science data structures, graph theory, resilience patterns, security primitives, text evaluation, and an interactive command-line interface.

---

## 2. Product Vision & Value Proposition

> *"Every essential algorithm and developer utility at your fingertips with zero `pip install` friction and zero supply-chain vulnerabilities."*

### Key Value Pillars
* **Zero External Dependencies:** Built strictly on Python's built-in standard library (`hashlib`, `hmac`, `math`, `collections`, `heapq`, `bisect`, `struct`, `urllib`).
* **Sub-Millisecond Cold Starts:** No heavy dynamic loading or third-party overhead.
* **100% Deterministic Testing:** Comprehensive unit tests covering boundary conditions, edge cases, and algorithmic correctness.
* **Dual Interface (Library + CLI):** Seamlessly importable in Python applications or executable from the terminal via [`cli.py`](file:///d:/ASHISH%20GITHUB/test-repo/cli.py).

---

## 3. User Personas & Use Cases

### Persona 1: Backend & Microservice Engineer (Alex)
* **Need:** Needs token-bucket rate limiting, circuit breaking, exponential backoff retries, and in-memory TTL caching without pulling in external Redis or heavy frameworks during initial prototyping or lightweight worker deployments.
* **Solution:** Imports [`src/rate_limiter.py`](file:///d:/ASHISH%20GITHUB/test-repo/src/rate_limiter.py), [`src/circuit_breaker.py`](file:///d:/ASHISH%20GITHUB/test-repo/src/circuit_breaker.py), and [`src/cache_utils.py`](file:///d:/ASHISH%20GITHUB/test-repo/src/cache_utils.py).

### Persona 2: DevOps & Infrastructure Engineer (Priya)
* **Need:** Needs fast terminal tools to compute subnet CIDRs, calculate CRC32 checksums, verify PBKDF2 hashes, generate TOTP codes, and explain complex cron schedules.
* **Solution:** Uses the interactive [`cli.py`](file:///d:/ASHISH%20GITHUB/test-repo/cli.py) subcommands (`cron-explain`, `totp-generate`, `checksum`, `disk-usage`).

### Persona 3: Library & SDK Maintainer (Marcus)
* **Need:** Wants to keep an open-source SDK minimal and lightweight, needing SemVer matching (`^1.2.0`), JSON pointer navigation (RFC 6901), and natural sorting without adding third-party requirements to `setup.py` / `pyproject.toml`.
* **Solution:** Embeds `DevToolkit` modules directly into the codebase.

---

## 4. Feature Requirements & Scope

### 4.1 Advanced Computer Science Data Structures
| Feature ID | Requirement | Acceptance Criteria |
|---|---|---|
| **DS-01** | Scalable Bloom Filter | Must dynamically spawn sub-filters when error capacity thresholds are reached while tightening error probability bounds. |
| **DS-02** | Counting Bloom Filter | Must support item frequency tracking and decrementing/deletion without corrupting the filter. |
| **DS-03** | Fenwick Tree (BIT) | Must compute dynamic prefix sums and point updates in $O(\log n)$. |
| **DS-04** | Segment Tree | Must handle range queries and point updates for arbitrary associative functions. |
| **DS-05** | Skip List | Must provide probabilistic $O(\log n)$ ordered search, insert, and delete. |
| **DS-06** | Treap (Cartesian Tree) | Must maintain BST ordering on keys and heap ordering on random priorities with $O(\log n)$ expected depth. |
| **DS-07** | $O(1)$ LFU Cache | Must evict least-frequently-used keys in $O(1)$ with LRU tie-breaking. |
| **DS-08** | Circular Ring Buffer | Fixed-capacity FIFO buffer supporting overwrite mode or overflow exceptions. |
| **DS-09** | Radix Tree (Patricia) | Compressed prefix tree merging common edges for space-optimal lookups. |
| **DS-10** | Sparse Matrix (DOK) | Memory-efficient dictionary-of-keys sparse matrix supporting addition and scaling. |

### 4.2 Graph & Combinatorial Algorithms
| Feature ID | Requirement | Acceptance Criteria |
|---|---|---|
| **GR-01** | A* 2D Grid Pathfinding | Finds optimal obstacle-avoiding paths using Manhattan and Euclidean heuristics. |
| **GR-02** | Tarjan's SCC | Identifies all strongly connected components in directed graphs in $O(V + E)$. |
| **GR-03** | Dijkstra's Algorithm | Computes single-source shortest path on positive-weighted directed/undirected graphs. |
| **GR-04** | Bellman-Ford | Computes shortest paths with arbitrary edge weights and flags negative weight cycles. |
| **GR-05** | Hopcroft-Karp Matching | Solves maximum cardinality bipartite matching in $O(E\sqrt{V})$. |
| **GR-06** | Minimum Spanning Tree | Implements Kruskal (DSU) and Prim (Priority Queue) algorithms for minimum cost trees. |
| **GR-07** | Hungarian Algorithm | Solves optimal linear sum assignment problem on cost matrices in $O(N^3)$. |

### 4.3 Text, Encoding & Mathematical Processing
| Feature ID | Requirement | Acceptance Criteria |
|---|---|---|
| **TX-01** | Shunting-Yard Evaluator | Evaluates math expressions with parentheses, operator precedence (`+`, `-`, `*`, `/`, `^`, `%`). |
| **TX-02** | Suffix Array & LRS | Builds suffix array via sorting and computes longest repeated substring (LRS). |
| **TX-03** | Levenshtein Automaton | Evaluates edit distance and performs fuzzy vocabulary matching within $k$ edits. |
| **TX-04** | Lossless RLE & Huffman | Bit-level Huffman prefix tree compression and byte/text Run-Length Encoding. |
| **TX-05** | RFC 6238 TOTP / HOTP | Generates and verifies time-based and counter-based one-time passwords. |
| **TX-06** | Arbitrary-Precision Money | Avoids float drift using base integer units and distributes remainders fairly. |

### 4.4 Command Line Interface (CLI)
* The CLI must provide `--help` documentation for all commands.
* Return exit code `0` on success and non-zero on failure or invalid arguments.
* Interactive subcommands include: `b62-encode`, `b62-decode`, `totp-generate`, `totp-verify`, `cron-explain`, `isbn-validate`, `rle-encode`, `rle-decode`, `geo-bearing`, `color-palette`, and 30+ others.

---

## 5. Non-Functional Requirements (NFR)

* **Performance:** Core utility functions must execute in under 1 millisecond. Test suite of 340+ tests must complete in under 30 seconds.
* **Compatibility:** Fully compliant with Python 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, and 3.14.
* **Quality Assurance:** 100% test pass rate on every commit with zero external test harness requirements (`unittest` standard library).
* **Security:** PBKDF2 hashing with recommended iteration counts, safe secrets generation via standard `secrets` module, zero shell execution injections.

---

## 6. Release & Versioning Strategy

`DevToolkit` follows **Semantic Versioning 2.0.0 (SemVer)**:
* **MAJOR (X.y.z):** Breaking API changes or function signature deprecations.
* **MINOR (x.Y.z):** Backward-compatible new modules, data structures, or CLI subcommands.
* **PATCH (x.y.Z):** Bug fixes, performance optimizations, or documentation revisions.
