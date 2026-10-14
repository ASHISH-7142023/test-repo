"""Configuration file parsing (INI and key-value formats) and dictionary merging."""

import io
import configparser
from typing import Dict, Any, Optional


def parse_ini_string(ini_text: str) -> Dict[str, Dict[str, str]]:
    """Parse an INI-formatted string into a nested dictionary of sections and options."""
    parser = configparser.ConfigParser()
    parser.read_string(ini_text)
    result = {}
    for section in parser.sections():
        result[section] = dict(parser[section])
    return result


def parse_key_value_string(text: str, delimiter: str = "=", comment_prefix: str = "#") -> Dict[str, str]:
    """Parse simple KEY=VALUE formatted lines (like .env or config files) into a dictionary."""
    result: Dict[str, str] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith(comment_prefix):
            continue
        if delimiter in line:
            key, val = line.split(delimiter, 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            result[key] = val
    return result


def serialize_ini(config_dict: Dict[str, Dict[str, Any]]) -> str:
    """Serialize a nested dictionary into INI format string."""
    parser = configparser.ConfigParser()
    for section, options in config_dict.items():
        parser[section] = {str(k): str(v) for k, v in options.items()}
    out = io.StringIO()
    parser.write(out)
    return out.getvalue()
