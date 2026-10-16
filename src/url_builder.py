"""Fluent URL and URI builder with chaining methods."""

import urllib.parse
from typing import Any, Dict, List


class URLBuilder:
    """Fluent chaining builder for constructing HTTP/HTTPS URLs."""

    def __init__(self, base_url: str = ""):
        self.scheme = "https"
        self.host = ""
        self.port: int = None
        self.path_segments: List[str] = []
        self.params: Dict[str, Any] = {}

        if base_url:
            parsed = urllib.parse.urlparse(base_url)
            self.scheme = parsed.scheme or "https"
            self.host = parsed.hostname or ""
            self.port = parsed.port
            if parsed.path and parsed.path != "/":
                self.path_segments = [seg for seg in parsed.path.split("/") if seg]

    def set_scheme(self, scheme: str) -> "URLBuilder":
        self.scheme = scheme
        return self

    def set_host(self, host: str) -> "URLBuilder":
        self.host = host
        return self

    def add_path(self, *segments: str) -> "URLBuilder":
        for seg in segments:
            clean = seg.strip("/")
            if clean:
                self.path_segments.append(clean)
        return self

    def add_param(self, key: str, value: Any) -> "URLBuilder":
        self.params[key] = value
        return self

    def build(self) -> str:
        netloc = self.host
        if self.port:
            netloc = f"{netloc}:{self.port}"
        path = "/" + "/".join(self.path_segments) if self.path_segments else "/"
        query = urllib.parse.urlencode(self.params) if self.params else ""
        return urllib.parse.urlunparse((self.scheme, netloc, path, "", query, ""))
