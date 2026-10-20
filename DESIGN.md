# 🎨 Algorithmic & API Design Document

## Project: `DevToolkit`
**Version:** 1.4.0  
**Focus:** Mathematical Foundations, Algorithmic Patterns, and API Conventions  

---

## 1. Algorithmic Design Patterns

`DevToolkit` modules are designed following mathematically optimal paradigms to ensure minimal asymptotic runtime and memory overhead.

### 1.1 Double Hashing & Scalable Bloom Filter Design
Standard Bloom filters degrade as the number of inserted elements exceeds the initial capacity $n$. `ScalableBloomFilter` solves this by orchestrating a dynamic sequence of sub-filters $F_0, F_1, F_2, \dots$:

* **Capacity Progression:** $S_i = S_0 \times s^i$ (where $s=2$ is the scale factor).
* **Error Rate Tightening:** $P_i = P_0 \times r^i$ (where $r=0.85$ is the tightening ratio).
* **Kirsch-Mitzenmacher Hash Optimization:** Rather than computing $k$ independent SHA-256 hashes, we compute two 64-bit base hashes $h_1, h_2$ and derive $k$ probes using:
  $$g_i(x) = (h_1 + i \times \text{step}) \pmod m$$
  $$\text{where } \text{step} = (h_2 \pmod{m - 1}) + 1 \quad (\text{guaranteeing } \text{step} \not\equiv 0 \pmod m)$$

---

### 1.2 Binary Indexed Tree (Fenwick Tree) Design
For prefix sum queries and point updates on dynamic arrays:
* **Storage:** 1-indexed array of length $N + 1$.
* **Least Significant Bit (LSB):** Navigation uses two's complement bitwise arithmetic:
  $$\text{LSB}(i) = i \ \& \ (-i)$$
* **Update Operation:** Propagates additions upward: $i \leftarrow i + \text{LSB}(i)$ in $O(\log N)$.
* **Prefix Query:** Accumulates sums downward: $i \leftarrow i - \text{LSB}(i)$ in $O(\log N)$.
* **Range Sum:** $\text{range\_sum}(L, R) = \text{prefix\_sum}(R) - \text{prefix\_sum}(L - 1)$ in $O(\log N)$.

---

### 1.3 $O(1)$ LFU Cache Design (Least Frequently Used)
Standard LFU implementations use heaps ($O(\log N)$) or linear scans ($O(N)$). `LFUCache` achieves strict **$O(1)$ amortized get and put** operations:

```
[Key to Val Map]       [Key to Freq Map]      [Frequency to Keys Map]
 "A" -> 100               "A" -> 2              Freq 1: OrderedDict(["C"])
 "B" -> 200               "B" -> 2              Freq 2: OrderedDict(["A", "B"])
 "C" -> 300               "C" -> 1              Freq 3: ...
```

* **Data Structures:**
  1. `key_to_val: Dict[K, V]`
  2. `key_to_freq: Dict[K, int]`
  3. `freq_to_keys: Dict[int, OrderedDict[K, None]]`
  4. `min_freq: int` pointer
* **Eviction Policy:** When capacity is exceeded, evict `freq_to_keys[min_freq].popitem(last=False)`. Because keys within a frequency bucket are ordered by insertion, tie-breaking is strictly **Least Recently Used (LRU)**.

---

### 1.4 Kuhn-Munkres (Hungarian) Assignment Design
Solves the minimum-cost linear sum assignment on an $N \times M$ bipartite graph ($N \le M$):
* **Dual Problem:** Introduces potentials $u_i$ (row) and $v_j$ (column) satisfying $u_i + v_j \le C_{ij}$.
* **Slack Array:** Maintains `minv[j]` tracking shortest distances to unvisited columns.
* **Complexity:** Runs in $O(N^2 M) = O(N^3)$ operations, avoiding factorial permutations.

---

### 1.5 Rate Limiting: Token Bucket Algorithm
Implemented in [`src/rate_limiter.py`](file:///d:/ASHISH%20GITHUB/test-repo/src/rate_limiter.py):
* **State:** `tokens: float`, `last_refill: float`, `rate: float`, `capacity: float`.
* **Lazy Refill Equation:**
  $$\text{tokens}_{\text{now}} = \min(\text{capacity}, \text{tokens}_{\text{prev}} + (\text{now} - \text{last\_refill}) \times \text{rate})$$
* **No Background Thread:** Uses `time.monotonic()` on access. Zero thread spinlocks or background worker tasks needed.

---

### 1.6 Arbitrary-Precision Financial Money Arithmetic
Avoids floating-point roundoff errors (e.g. `0.1 + 0.2 != 0.3`):
* **Integer Representation:** Monetary values are stored as integer base units (e.g., $10.50 \rightarrow 1050\text{ cents}$).
* **Fair Splitting Algorithm:** When dividing money among $N$ recipients, remaining cents are allocated one-by-one to the first $R = \text{units} \pmod N$ recipients, ensuring:
  $$\sum_{i=1}^N \text{part}_i = \text{total\_units} \quad (\text{exact conservation of currency})$$

---

## 2. API Design Conventions

### 2.1 Function & Method Signatures
1. **Explicit Typing:** All functions must specify type annotations for arguments and return types.
   ```python
   def rle_encode(text: str) -> str: ...
   def convert_length(value: float, from_unit: str, to_unit: str) -> float: ...
   ```
2. **Fail-Fast Validation:** Raise descriptive, standard Python exceptions:
   * `ValueError` for out-of-range bounds, invalid strings, or dimensions.
   * `TypeError` for incorrect argument types.
   * `IndexError` for out-of-bounds matrix or spatial index queries.

### 2.2 Error Handling & Resilience
* Network or algorithmic fallbacks should degrade gracefully (e.g., `resolve_json_pointer` returns `default` on non-existent keys rather than crashing).
* Cryptographic functions must use constant-time comparisons (`hmac.compare_digest`) to protect against timing attacks.
