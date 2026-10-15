"""Semantic Versioning (SemVer 2.0.0) parsing, comparison, and increment helpers."""

import re
from typing import Tuple

_SEMVER_REGEX = re.compile(
    r"^v?(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)"
    r"(?:-(?P<prerelease>[0-9A-Za-z.-]+))?"
    r"(?:\+(?P<buildmetadata>[0-9A-Za-z.-]+))?$"
)


def parse_semver(version: str) -> Tuple[int, int, int]:
    """Parse semver string into (major, minor, patch) tuple."""
    m = _SEMVER_REGEX.match(version.strip())
    if not m:
        raise ValueError(f"Invalid semantic version: '{version}'")
    return int(m.group("major")), int(m.group("minor")), int(m.group("patch"))


def is_valid_semver(version: str) -> bool:
    """Validate whether version string conforms to SemVer format."""
    return bool(_SEMVER_REGEX.match(version.strip()))


def compare_semver(v1: str, v2: str) -> int:
    """Compare two semver strings: returns -1 if v1 < v2, 0 if v1 == v2, 1 if v1 > v2."""
    t1 = parse_semver(v1)
    t2 = parse_semver(v2)
    if t1 < t2:
        return -1
    elif t1 > t2:
        return 1
    return 0


def bump_semver(version: str, component: str = "patch") -> str:
    """Bump major, minor, or patch component of semver string."""
    maj, minr, patch = parse_semver(version)
    if component == "major":
        return f"{maj + 1}.0.0"
    elif component == "minor":
        return f"{maj}.{minr + 1}.0"
    elif component == "patch":
        return f"{maj}.{minr}.{patch + 1}"
    raise ValueError(f"Invalid component '{component}'; expected 'major', 'minor', or 'patch'.")
