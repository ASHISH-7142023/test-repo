"""Fluent Markdown document and badge structure builder."""

from typing import List, Sequence


class MarkdownBuilder:
    """Fluent chaining builder for generating Markdown documents."""

    def __init__(self):
        self._lines: List[str] = []

    def header(self, text: str, level: int = 1) -> "MarkdownBuilder":
        prefix = "#" * max(1, min(level, 6))
        self._lines.append(f"{prefix} {text}\n")
        return self

    def paragraph(self, text: str) -> "MarkdownBuilder":
        self._lines.append(f"{text}\n")
        return self

    def bullet_list(self, items: Sequence[str]) -> "MarkdownBuilder":
        for item in items:
            self._lines.append(f"- {item}")
        self._lines.append("")
        return self

    def code_block(self, code: str, language: str = "") -> "MarkdownBuilder":
        self._lines.append(f"```{language}")
        self._lines.append(code.strip())
        self._lines.append("```\n")
        return self

    def badge(self, label: str, message: str, color: str = "blue") -> str:
        return f"![{label}](https://img.shields.io/badge/{label}-{message}-{color}.svg)"

    def build(self) -> str:
        return "\n".join(self._lines).strip()
