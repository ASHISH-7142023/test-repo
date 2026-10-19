#!/usr/bin/env python3
"""Unified command-line interface for DevToolkit."""

import sys
import argparse
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
from src.security_utils import hash_password, verify_password
from src.net_utils import is_valid_ipv4, is_private_ip
from src.humanize_utils import ordinal, intcomma
from src.semver_utils import bump_semver
from src.currency_utils import format_currency
from src.luhn_utils import validate_luhn
from src.color_contrast import contrast_ratio, is_wcag_aa
from src.mime_utils import guess_mime_type
from src.base58_utils import b58encode, b58decode
from src.phonetic_utils import soundex, soundex_matches
from src.morse_code import text_to_morse, morse_to_text
from src.roman_numerals import to_roman, from_roman
from src.units_converter import convert_length, convert_weight, convert_temperature, convert_bytes
from src.base62_utils import base62_encode_int, base62_decode_int
from src.totp_utils import totp, verify_totp
from src.cron_parser import explain_cron
from src.isbn_utils import validate_isbn10, validate_isbn13, isbn10_to_isbn13
from src.color_cmyk import rgb_to_cmyk


def main():
    parser = argparse.ArgumentParser(description="DevToolkit CLI Utilities")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # String & Text
    p_slug = subparsers.add_parser("slug", help="Convert text into an ASCII slug")
    p_slug.add_argument("text", help="Text to slugify")

    p_mask = subparsers.add_parser("mask", help="Mask sensitive token or number")
    p_mask.add_argument("text", help="Text to mask")
    p_mask.add_argument("--visible", type=int, default=4, help="Number of trailing characters visible")

    # Morse
    p_me = subparsers.add_parser("morse-encode", help="Encode text to Morse code")
    p_me.add_argument("text", help="Text to encode")

    p_md = subparsers.add_parser("morse-decode", help="Decode Morse code to text")
    p_md.add_argument("morse", help="Morse code with spaces between letters and / between words")

    # Roman
    p_tr = subparsers.add_parser("to-roman", help="Convert integer to Roman numeral")
    p_tr.add_argument("number", type=int, help="Integer (1-3999)")

    p_fr = subparsers.add_parser("from-roman", help="Convert Roman numeral to integer")
    p_fr.add_argument("roman", help="Roman numeral string")

    # Units
    p_uc = subparsers.add_parser("convert-units", help="Convert length units (m, km, mi, ft, etc.)")
    p_uc.add_argument("val", type=float, help="Value to convert")
    p_uc.add_argument("from_unit", help="Source unit")
    p_uc.add_argument("to_unit", help="Target unit")

    # CMYK
    p_cmyk = subparsers.add_parser("rgb-to-cmyk", help="Convert RGB to CMYK percentages")
    p_cmyk.add_argument("r", type=int, help="Red (0-255)")
    p_cmyk.add_argument("g", type=int, help="Green (0-255)")
    p_cmyk.add_argument("b", type=int, help="Blue (0-255)")

    # MIME
    p_mime = subparsers.add_parser("guess-mime", help="Detect MIME type from file extension")
    p_mime.add_argument("path", help="Filename or extension")

    # Base58
    p_b58e = subparsers.add_parser("b58-encode", help="Encode text to Base58")
    p_b58e.add_argument("text", help="Text to encode")

    p_b58d = subparsers.add_parser("b58-decode", help="Decode Base58 string")
    p_b58d.add_argument("encoded", help="Base58 string")

    # Phonetics
    p_snd = subparsers.add_parser("soundex", help="Compute Soundex phonetic code")
    p_snd.add_argument("word", help="English name or word")

    p_sndm = subparsers.add_parser("soundex-match", help="Check if two names match in Soundex")
    p_sndm.add_argument("w1", help="First word")
    p_sndm.add_argument("w2", help="Second word")

    # Luhn
    p_luhn = subparsers.add_parser("luhn-check", help="Verify card number with Luhn algorithm")
    p_luhn.add_argument("number", help="Credit card or account number")

    # Contrast
    p_contrast = subparsers.add_parser("contrast", help="Compute WCAG color contrast ratio")
    p_contrast.add_argument("fg", help="Foreground hex color (#fff)")
    p_contrast.add_argument("bg", help="Background hex color (#000)")

    # SemVer
    p_semver = subparsers.add_parser("semver-bump", help="Bump semantic version")
    p_semver.add_argument("version", help="Current version string")
    p_semver.add_argument("--type", choices=["major", "minor", "patch"], default="patch")

    # Currency
    p_curr = subparsers.add_parser("currency", help="Format currency amount")
    p_curr.add_argument("amount", type=float, help="Numeric value")
    p_curr.add_argument("--code", default="USD", help="Currency code (USD, EUR, INR)")

    # UUID
    p_uuid = subparsers.add_parser("uuid", help="Generate UUIDv4")
    p_uuid.add_argument("--short", action="store_true", help="Generate 22-character short UUID")

    # Security & Password
    p_hash_pw = subparsers.add_parser("hash-password", help="Hash password using PBKDF2-HMAC-SHA256")
    p_hash_pw.add_argument("password", help="Password to hash")

    p_verify_pw = subparsers.add_parser("verify-password", help="Verify password against PBKDF2 hash")
    p_verify_pw.add_argument("password", help="Plain password")
    p_verify_pw.add_argument("hash", help="Hashed string")

    # Network
    p_ip = subparsers.add_parser("ip-info", help="Inspect IP address validity and privacy")
    p_ip.add_argument("ip", help="IP address to check")

    # Humanize
    p_ord = subparsers.add_parser("ordinal", help="Format integer with ordinal suffix")
    p_ord.add_argument("number", type=int, help="Integer value")

    p_comma = subparsers.add_parser("intcomma", help="Format number with commas")
    p_comma.add_argument("number", type=int, help="Integer value")

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


    # Base62 commands
    b62_enc_p = subparsers.add_parser("b62-encode", help="Encode integer to Base62")
    b62_enc_p.add_argument("num", type=int, help="Non-negative integer")

    b62_dec_p = subparsers.add_parser("b62-decode", help="Decode Base62 string to integer")
    b62_dec_p.add_argument("code", help="Base62 string")

    # TOTP commands
    totp_gen_p = subparsers.add_parser("totp-generate", help="Generate TOTP code from secret")
    totp_gen_p.add_argument("secret", help="Base32 or string secret")

    totp_ver_p = subparsers.add_parser("totp-verify", help="Verify TOTP code against secret")
    totp_ver_p.add_argument("secret", help="Base32 or string secret")
    totp_ver_p.add_argument("token", help="6-digit token")

    # Cron explain
    cron_exp_p = subparsers.add_parser("cron-explain", help="Explain 5-field cron expression")
    cron_exp_p.add_argument("expression", help="Cron string, e.g. '*/5 * * * *'")

    # ISBN validate
    isbn_p = subparsers.add_parser("isbn-validate", help="Validate ISBN-10 or ISBN-13")
    isbn_p.add_argument("isbn", help="ISBN string")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "slug":
        print(slugify(args.text))
    elif args.command == "mask":
        print(mask_sensitive(args.text, visible_chars=args.visible))
    elif args.command == "morse-encode":
        print(text_to_morse(args.text))
    elif args.command == "morse-decode":
        print(morse_to_text(args.morse))
    elif args.command == "to-roman":
        print(to_roman(args.number))
    elif args.command == "from-roman":
        print(from_roman(args.roman))
    elif args.command == "convert-units":
        print(convert_length(args.val, args.from_unit, args.to_unit))
    elif args.command == "rgb-to-cmyk":
        c, m, y, k = rgb_to_cmyk(args.r, args.g, args.b)
        print(f"C: {c}%, M: {m}%, Y: {y}%, K: {k}%")
    elif args.command == "guess-mime":
        print(guess_mime_type(args.path))
    elif args.command == "b58-encode":
        print(b58encode(args.text))
    elif args.command == "b58-decode":
        print(b58decode(args.encoded).decode("utf-8", errors="replace"))
    elif args.command == "soundex":
        print(soundex(args.word))
    elif args.command == "soundex-match":
        matches = soundex_matches(args.w1, args.w2)
        print(colorize(f"Soundex Match: {matches}", GREEN if matches else YELLOW))
        sys.exit(0 if matches else 1)
    elif args.command == "luhn-check":
        valid = validate_luhn(args.number)
        print(colorize(f"Luhn Valid: {valid}", GREEN if valid else YELLOW))
        sys.exit(0 if valid else 1)
    elif args.command == "contrast":
        ratio = contrast_ratio(args.fg, args.bg)
        aa = is_wcag_aa(args.fg, args.bg)
        print(f"Contrast Ratio: {ratio}:1 | WCAG AA: {aa}")
    elif args.command == "semver-bump":
        print(bump_semver(args.version, args.type))
    elif args.command == "currency":
        print(format_currency(args.amount, args.code))
    elif args.command == "uuid":
        print(short_uuid() if args.short else generate_uuid4())
    elif args.command == "hash-password":
        print(hash_password(args.password, iterations=10_000))
    elif args.command == "verify-password":
        valid = verify_password(args.password, args.hash)
        print(colorize("Password matches!", GREEN) if valid else colorize("Password invalid!", YELLOW))
        sys.exit(0 if valid else 1)
    elif args.command == "ip-info":
        valid_v4 = is_valid_ipv4(args.ip)
        private = is_private_ip(args.ip) if valid_v4 else False
        print(f"Valid IPv4: {valid_v4} | Private Subnet: {private}")
    elif args.command == "ordinal":
        print(ordinal(args.number))
    elif args.command == "intcomma":
        print(intcomma(args.number))
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

    elif args.command == "b62-encode":
        print(base62_encode_int(args.num))
    elif args.command == "b62-decode":
        print(base62_decode_int(args.code))
    elif args.command == "totp-generate":
        print(totp(args.secret))
    elif args.command == "totp-verify":
        valid = verify_totp(args.token, args.secret)
        print("Valid" if valid else "Invalid")
        sys.exit(0 if valid else 1)
    elif args.command == "cron-explain":
        print(explain_cron(args.expression))
    elif args.command == "isbn-validate":
        v10 = validate_isbn10(args.isbn)
        v13 = validate_isbn13(args.isbn)
        if v10:
            print(f"Valid ISBN-10 (ISBN-13: {isbn10_to_isbn13(args.isbn)})")
        elif v13:
            print("Valid ISBN-13")
        else:
            print("Invalid ISBN")
            sys.exit(1)



if __name__ == "__main__":
    main()
