# 🧠 Repository Memory & Technical Context

## Project: `DevToolkit`
**Repository:** `ASHISH-7142023/test-repo`  
**Current Branch:** `main`  
**Commit Milestones:** 306 Authentic Commits  
**Last Verified Version:** v1.4.0  

---

## 1. Project Background & Evolution

The repository was structured to build **`DevToolkit`**, a lightweight, zero-dependency developer utility suite and standard library extension for Python. Over multiple iterative development cycles, genuine, fully functional computer science data structures, graph algorithms, cryptographic utilities, text processors, and CLI tools were introduced.

### Development History & Commit Batches
* **Initial Setup & Cleanup:** Cleaned legacy skeleton and established standard project structure (`src/`, `tests/`, `cli.py`, `pyproject.toml`).
* **Batch 1 (11 commits):** Core string, date, math, collection, and UUID helpers.
* **Batch 2 (16 commits):** File operations, crypto tokens, system metrics, environment loaders, and colorizers.
* **Batch 3 (17 commits):** TTL Cache, token-bucket rate limiter, benchmark timers, CSV utilities, and structured logger.
* **Batch 4 (33 commits):** Binary search, bitwise utils, Boyer-Moore, base32, slug generation, and CLI subcommands.
* **Batch 5 (37 commits):** Levenshtein distance, net utilities, stopwatches, fractions, event bus, and resilience patterns.
* **Batch 6 (35 commits):** Matrix math, stats, regex patterns, tree serializers, and GitHub Actions CI matrix.
* **Batch 7 (42 commits):** Ring buffers, Dijkstra's algorithm, skip lists, interval trees, base58, and soundex.
* **Batch 8 (45 commits):** Suffix arrays, Tarjan's SCC, A* grid pathfinder, Fenwick tree, segment tree, Huffman compression, and Roman numerals.
* **Batch 9 (32 commits):** Scalable Bloom filter, LFU cache, Treap, Levenshtein automaton, k-d tree, Bellman-Ford, Hopcroft-Karp, TOTP/HOTP, and ISBN utilities.
* **Batch 10 (29 commits):** BitField packing, RLE compression, color palettes, Vincenty/Haversine geodesics, sparse matrices, Hungarian assignment, and consistent hash rings.

---

## 2. Established Patterns & Conventions

### 2.1 The "Zero-Dependency" Rule
* No external packages (e.g. `requests`, `numpy`, `scipy`, `pydantic`) may ever be added to runtime dependencies.
* Any feature must be implemented cleanly using standard library modules (`collections`, `heapq`, `bisect`, `struct`, `hashlib`, `hmac`, `math`, `re`).

### 2.2 Granular Conventional Commits
All commits follow the Conventional Commits specification:
* `feat(<module>): ...` — Implements the source module under `src/`.
* `test(<module>): ...` — Implements comprehensive unit tests under `tests/`.
* `refactor(cli): ...` — Registers new subcommands in `cli.py`.
* `test(cli): ...` — Integration tests for CLI arguments and dispatch.
* `chore(package): ...` — Updates `pyproject.toml` version metadata.
* `docs: ...` — Updates `README.md` and project documentation.

---

## 3. Key Technical Learnings & Critical Gotchas

> [!IMPORTANT]
> **Kirsch-Mitzenmacher Double Hashing Non-Zero Step Size**  
> In Bloom filters using double hashing $g_i(x) = (h_1 + i \cdot h_2) \pmod m$, if $h_2 \pmod m == 0$, all $k$ hashes collapse to $h_1 \pmod m$. Always calculate step as:
> `step = (h2 % (self.size - 1)) + 1 if self.size > 1 else 1`

> [!NOTE]
> **`DisjointSet` Type Subscripting**  
> `DisjointSet` is defined without generic subscripting in `src/disjoint_set.py`. Always instantiate via `dsu = DisjointSet()` rather than `DisjointSet[Any]()`.

> [!TIP]
> **SemVer 3-Tuple Return**  
> `src/semver_utils.py:parse_semver()` returns a 3-tuple `(major, minor, patch)` rather than a 4-tuple.

> [!WARNING]
> **Regex Escape Sequences in Python 3.12+**  
> Python 3.12+ emits `SyntaxWarning: invalid escape sequence` for unescaped regex strings. Always prefix regexes with `r"..."` or double escape backslashes `\\`.

> [!NOTE]
> **CLI Dispatch Integration**  
> When adding new commands to `cli.py`, ensure both:
> 1. The subparser argument declaration is added before `parser.parse_args()`.
> 2. The execution `elif args.command == "..."` is added in the dispatch chain before the fallback block.
