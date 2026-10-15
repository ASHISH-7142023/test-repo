"""Terminal ASCII and Markdown table formatting helpers."""

from typing import Any, List, Sequence


def format_ascii_table(headers: Sequence[str], rows: Sequence[Sequence[Any]]) -> str:
    """Generate a clean ASCII box table for terminal display."""
    str_headers = [str(h) for h in headers]
    str_rows = [[str(cell) for cell in row] for row in rows]
    cols = len(str_headers)

    col_widths = [len(h) for h in str_headers]
    for row in str_rows:
        for idx, cell in enumerate(row):
            if idx < cols:
                col_widths[idx] = max(col_widths[idx], len(cell))

    sep = "+-" + "-+-".join("-" * w for w in col_widths) + "-+"
    header_line = "| " + " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(str_headers)) + " |"

    body_lines = []
    for row in str_rows:
        line = "| " + " | ".join(row[i].ljust(col_widths[i]) if i < len(row) else "".ljust(col_widths[i]) for i in range(cols)) + " |"
        body_lines.append(line)

    return "\n".join([sep, header_line, sep] + body_lines + [sep])


def format_markdown_table(headers: Sequence[str], rows: Sequence[Sequence[Any]]) -> str:
    """Format data into standard GitHub-flavored markdown table."""
    str_headers = [str(h) for h in headers]
    header_row = "| " + " | ".join(str_headers) + " |"
    divider = "| " + " | ".join("---" for _ in str_headers) + " |"
    data_rows = ["| " + " | ".join(str(cell) for cell in row) + " |" for row in rows]
    return "\n".join([header_row, divider] + data_rows)
