"""Streaming CSV processing and serialization helpers."""

import csv
import io
from typing import List, Dict, Any, Optional, Iterable


def detect_delimiter(sample_text: str, default: str = ",") -> str:
    """Sniff CSV delimiter (comma, semicolon, tab, pipe) from sample text."""
    if not sample_text:
        return default
    try:
        dialect = csv.Sniffer().sniff(sample_text[:4096])
        return dialect.delimiter
    except csv.Error:
        return default


def read_csv_dicts(content: str, delimiter: Optional[str] = None) -> List[Dict[str, str]]:
    """Parse CSV text into list of row dictionaries."""
    if not content.strip():
        return []
    if delimiter is None:
        delimiter = detect_delimiter(content)
    f = io.StringIO(content.strip())
    reader = csv.DictReader(f, delimiter=delimiter)
    return [dict(row) for row in reader]


def write_csv_dicts(rows: List[Dict[str, Any]], fieldnames: Optional[List[str]] = None, delimiter: str = ",") -> str:
    """Serialize list of dictionaries into formatted CSV string."""
    if not rows:
        return ""
    if fieldnames is None:
        fieldnames = list(rows[0].keys())
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=delimiter, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    return output.getvalue()
