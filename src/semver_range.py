"""Semantic version range comparator supporting ranges like >=1.2.0, ^1.0.0, ~1.2.0."""

import re
from src.semver_utils import parse_semver, compare_semver


def _check_single_condition(version: str, cond: str) -> bool:
    cond = cond.strip()
    if not cond or cond == "*":
        return True

    if cond.startswith("^"):
        base = cond[1:]
        major, minor, patch = parse_semver(base)
        upper = f"{major + 1}.0.0" if major > 0 else f"0.{minor + 1}.0"
        return compare_semver(version, base) >= 0 and compare_semver(version, upper) < 0

    if cond.startswith("~"):
        base = cond[1:]
        major, minor, patch = parse_semver(base)
        upper = f"{major}.{minor + 1}.0"
        return compare_semver(version, base) >= 0 and compare_semver(version, upper) < 0

    match = re.match(r"^(>=|<=|>|<|=)?\s*([0-9A-Za-z.\-+]+)$", cond)
    if not match:
        raise ValueError(f"Invalid condition: '{cond}'")

    op, target = match.groups()
    op = op or "="
    cmp_res = compare_semver(version, target)

    if op == "=":
        return cmp_res == 0
    elif op == ">":
        return cmp_res > 0
    elif op == ">=":
        return cmp_res >= 0
    elif op == "<":
        return cmp_res < 0
    elif op == "<=":
        return cmp_res <= 0
    return False


def satisfies_range(version: str, range_spec: str) -> bool:
    """Check if a semver string satisfies space-delimited AND conditions."""
    for cond in range_spec.split():
        if not _check_single_condition(version, cond):
            return False
    return True
