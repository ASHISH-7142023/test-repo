#!/usr/bin/env python3
"""Unified command-line interface for DevToolkit."""

import sys
import argparse
import time
from src.string_utils import slugify, mask_sensitive
from src.date_utils import human_readable_duration
from src.validators import is_valid_email, is_strong_password
from src.math_utils import percent_change
from src.encoding_utils import to_base64, from_base64
from src.crypto_utils import generate_secure_token
from src.file_utils import get_file_checksum
from src.uuid_utils import generate_uuid4, short_uuid
from src.system_utils import get_platform_info, get_disk_usage
from src.color_utils import colorize, GREEN, CYAN, YELLOW, BOLD


def main():
    parser = argparse.ArgumentParser(description="DevToolkit CLI Utilities")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # String & Text
    p_slug = subparsers.add_parser("slug", help="Convert text into an ASCII slug")
    p_slug.add_argument("text", help="Text to slugify")

    p_mask = subparsers.add_parser("mask", help="Mask sensitive token or number")
    p_mask.add_argument("text", help="Text to mask")
    p_mask.add_argument("--visible", type=int, default=4, help="Number of trailing characters visible")

    # UUID
    p_uuid = subparsers.add_parser("uuid", help="Generate UUIDv4")
    p_uuid.add_argument("--short", action="store_true", help="Generate 22-character short UUID")

    # Encoding
    p_b64e = subparsers.add_parser("b64-encode", help="Encode text to Base64")
    p_b64e.add_argument("text", help="String to encode")

    p_b64d = subparsers.add_parser("b64-decode", help="Decode Base64 string")
    p_b64d.add_argument("encoded", help="Base64 string to decode")

    # Cryptography
    p_token = subparsers.add_parser("token", help="Generate secure random token")
    p_token.add_argument("--bytes", type=int, default=32, help="Number of random bytes")

    p_hash = subparsers.add_parser("checksum", help="Calculate SHA256 checksum of a file")
    p_hash.add_argument("path", help="Path to file")

    # System Diagnostics
    subparsers.add_parser("sys-info", help="Print OS and hardware platform details")
    subparsers.add_parser("disk-usage", help="Print disk space usage summary")

    # DateTime & Math
    p_dur = subparsers.add_parser("duration", help="Format seconds to duration")
    p_dur.add_argument("seconds", type=int, help="Total seconds")

    p_pct = subparsers.add_parser("pct-change", help="Calculate percentage change")
    p_pct.add_argument("initial", type=float, help="Initial value")
    p_pct.add_argument("final", type=float, help="Final value")

    # Validators
    p_email = subparsers.add_parser("validate-email", help="Check if an email format is valid")
    p_email.add_argument("email", help="Email address")

    p_pass = subparsers.add_parser("validate-password", help="Audit password strength")
    p_pass.add_argument("password", help="Password string")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "slug":
        print(slugify(args.text))
    elif args.command == "mask":
        print(mask_sensitive(args.text, visible_chars=args.visible))
    elif args.command == "uuid":
        if args.short:
            print(short_uuid())
        else:
            print(generate_uuid4())
    elif args.command == "sys-info":
        info = get_platform_info()
        print(colorize(f"System: {info['system']} {info['release']} ({info['machine']})", CYAN))
        print(colorize(f"Python: {info['python_version']}", GREEN))
    elif args.command == "disk-usage":
        disk = get_disk_usage(".")
        print(f"Total: {disk['total_formatted']} | Used: {disk['used_formatted']} ({disk['percent_used']}%) | Free: {disk['free_formatted']}")
    elif args.command == "b64-encode":
        print(to_base64(args.text))
    elif args.command == "b64-decode":
        print(from_base64(args.encoded))
    elif args.command == "token":
        print(generate_secure_token(args.bytes))
    elif args.command == "checksum":
        print(get_file_checksum(args.path))
    elif args.command == "duration":
        print(human_readable_duration(args.seconds))
    elif args.command == "pct-change":
        print(f"{percent_change(args.initial, args.final)}%")
    elif args.command == "validate-email":
        valid = is_valid_email(args.email)
        print(colorize(f"Valid: {valid}", GREEN if valid else YELLOW))
        sys.exit(0 if valid else 1)
    elif args.command == "validate-password":
        valid, issues = is_strong_password(args.password)
        if valid:
            print(colorize("Password satisfies complexity requirements.", GREEN))
        else:
            print(colorize("Password issues found:", YELLOW))
            for issue in issues:
                print(f" - {issue}")
        sys.exit(0 if valid else 1)


if __name__ == "__main__":
    main()
