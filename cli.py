#!/usr/bin/env python3
"""Unified command-line interface for DevToolkit."""

import sys
import argparse
from src.string_utils import slugify, mask_sensitive
from src.date_utils import human_readable_duration, format_iso
from src.validators import is_valid_email, is_strong_password
from src.math_utils import percent_change, clamp


def main():
    parser = argparse.ArgumentParser(description="DevToolkit CLI Utilities")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Slugify command
    p_slug = subparsers.add_parser("slug", help="Convert text into an ASCII slug")
    p_slug.add_argument("text", help="Text to slugify")

    # Mask command
    p_mask = subparsers.add_parser("mask", help="Mask sensitive token or number")
    p_mask.add_argument("text", help="Text to mask")
    p_mask.add_argument("--visible", type=int, default=4, help="Number of trailing characters visible")

    # Duration command
    p_dur = subparsers.add_parser("duration", help="Format seconds to duration")
    p_dur.add_argument("seconds", type=int, help="Total seconds")

    # Validate email command
    p_email = subparsers.add_parser("validate-email", help="Check if an email format is valid")
    p_email.add_argument("email", help="Email address")

    # Validate password command
    p_pass = subparsers.add_parser("validate-password", help="Audit password strength")
    p_pass.add_argument("password", help="Password string")

    # Percent change command
    p_pct = subparsers.add_parser("pct-change", help="Calculate percentage change")
    p_pct.add_argument("initial", type=float, help="Initial value")
    p_pct.add_argument("final", type=float, help="Final value")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "slug":
        print(slugify(args.text))
    elif args.command == "mask":
        print(mask_sensitive(args.text, visible_chars=args.visible))
    elif args.command == "duration":
        print(human_readable_duration(args.seconds))
    elif args.command == "validate-email":
        valid = is_valid_email(args.email)
        print(f"Valid: {valid}")
        sys.exit(0 if valid else 1)
    elif args.command == "validate-password":
        valid, issues = is_strong_password(args.password)
        if valid:
            print("Password satisfies complexity requirements.")
        else:
            print("Password issues found:")
            for issue in issues:
                print(f" - {issue}")
        sys.exit(0 if valid else 1)
    elif args.command == "pct-change":
        print(f"{percent_change(args.initial, args.final)}%")


if __name__ == "__main__":
    main()
