"""
Unified Diff Line Parser & In-Memory Text Patcher.
Lightweight unified diff parser and patch application engine.
"""
import difflib

def create_unified_diff(original: str, modified: str, filename: str = "file") -> str:
    """Generate a unified diff between two text strings."""
    orig_lines = original.splitlines(keepends=True)
    mod_lines = modified.splitlines(keepends=True)
    diff = difflib.unified_diff(orig_lines, mod_lines, fromfile=f"a/{filename}", tofile=f"b/{filename}")
    return "".join(diff)

def apply_patch(original: str, patch_text: str) -> str:
    """
    Applies a simple unified diff patch to the original text string.
    """
    lines = original.splitlines()
    patch_lines = patch_text.splitlines()
    res = list(lines)

    target_idx = 0
    for line in patch_lines:
        if line.startswith("@@"):
            parts = line.split(" ")
            if len(parts) >= 3 and parts[1].startswith("-"):
                old_info = parts[1][1:].split(",")
                target_idx = max(0, int(old_info[0]) - 1)
        elif line.startswith("-") and not line.startswith("---"):
            if target_idx < len(res):
                res.pop(target_idx)
        elif line.startswith("+") and not line.startswith("+++"):
            res.insert(target_idx, line[1:])
            target_idx += 1
        elif line.startswith(" "):
            target_idx += 1
    return "\n".join(res)
