# 📜 Engineering Rules & Guidelines

## Project: `DevToolkit`
**Standard:** Strict Zero-Dependency Python Engineering  

---

## Rule 1: The Zero External Dependency Law
* **Absolute Constraint:** Never add any third-party dependencies to `pyproject.toml` or `src/`.
* **Standard Library Only:** Use only packages built into standard Python (`math`, `collections`, `heapq`, `bisect`, `struct`, `hashlib`, `hmac`, `re`, `difflib`, `secrets`, `time`, `datetime`, `urllib`).
* **Self-Contained:** Algorithms must be implemented from first principles.

---

## Rule 2: Python Compatibility (3.8 - 3.14+)
* Ensure complete compatibility from Python 3.8 upwards.
* **Type Hinting:** Use `from typing import List, Dict, Tuple, Optional, Any, Set, Union, Generic, TypeVar` for annotations to avoid runtime subscripting issues on Python 3.8.
* **Escape Warnings:** Always use raw string literals `r"..."` for regular expressions to eliminate `SyntaxWarning` on modern Python versions.

---

## Rule 3: Testing Mandate (100% Pass Rate)
* Every module in `src/<module>.py` **must** have a corresponding test module `tests/test_<module>.py`.
* Every test suite must run using standard `unittest`:
  ```bash
  python -m unittest discover tests -v
  ```
* **Zero Failure Tolerance:** Pushes to `origin/main` are forbidden if any test produces a failure or error.
* Tests must test:
  1. Happy path operations and typical inputs.
  2. Edge cases (empty sequences, single elements, large values).
  3. Error conditions (`assertRaises` for `ValueError`, `TypeError`, `IndexError`).

---

## Rule 4: Granular Conventional Commits
* **No Empty / Dummy Commits:** Never use `--allow-empty` or commit non-functional placeholder code.
* **Commit Message Format:**
  * `feat(<scope>): <description in imperative mood>`
  * `test(<scope>): <description>`
  * `refactor(<scope>): <description>`
  * `chore(<scope>): <description>`
  * `docs: <description>`
* **Atomic Scope:** Keep feature implementation and unit tests in separate or cleanly coupled granular commits.

---

## Rule 5: CLI Subcommand Standards
When adding a new command to [`cli.py`](file:///d:/ASHISH%20GITHUB/test-repo/cli.py):
1. Add a subparser with descriptive `help` text and argument definitions.
2. Implement the command execution branch under `args.command == "<name>"`.
3. Format output cleanly to standard output.
4. Exit with code `0` on success and non-zero (`sys.exit(1)`) on error.
5. Add an integration test in `tests/test_cli_commands_*.py`.

---

## Rule 6: Git Hygiene & Cleanliness
* No temporary or generator scripts (`make_*_commits.py`, `.temp*`, `.bak`) may remain untracked in the working tree.
* Working tree must be clean before and after every push (`git status` reports `nothing to commit, working tree clean`).
* Keep `README.md` and `pyproject.toml` in sync with active test counts and feature inventories.
