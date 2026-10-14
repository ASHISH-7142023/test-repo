"""Networking, IPv4/IPv6 validation, CIDR subnet matching, and port sanity checks."""

import ipaddress
from typing import Union


def is_valid_ipv4(ip: str) -> bool:
    """Validate whether input is a canonical IPv4 address."""
    try:
        addr = ipaddress.IPv4Address(ip.strip())
        return True
    except (ipaddress.AddressValueError, ValueError):
        return False


def is_valid_ipv6(ip: str) -> bool:
    """Validate whether input is a canonical IPv6 address."""
    try:
        addr = ipaddress.IPv6Address(ip.strip())
        return True
    except (ipaddress.AddressValueError, ValueError):
        return False


def is_private_ip(ip: str) -> bool:
    """Check if IPv4/IPv6 address is in a private RFC1918/RFC4193 range."""
    try:
        addr = ipaddress.ip_address(ip.strip())
        return addr.is_private
    except ValueError:
        return False


def ip_in_cidr(ip: str, cidr: str) -> bool:
    """Check whether an IP address belongs to a CIDR subnet range."""
    try:
        network = ipaddress.ip_network(cidr.strip(), strict=False)
        addr = ipaddress.ip_address(ip.strip())
        return addr in network
    except ValueError:
        return False


def is_valid_port(port: Union[int, str]) -> bool:
    """Check whether integer or string represents a valid TCP/UDP port (1-65535)."""
    try:
        p = int(port)
        return 1 <= p <= 65535
    except (ValueError, TypeError):
        return False
