"""Unit tests for networking and IP validation utilities."""

import unittest
from src.net_utils import (
    is_valid_ipv4,
    is_valid_ipv6,
    is_private_ip,
    ip_in_cidr,
    is_valid_port
)


class TestNetUtils(unittest.TestCase):

    def test_is_valid_ipv4(self):
        self.assertTrue(is_valid_ipv4("192.168.1.1"))
        self.assertTrue(is_valid_ipv4("8.8.8.8"))
        self.assertFalse(is_valid_ipv4("256.0.0.1"))
        self.assertFalse(is_valid_ipv4("not_an_ip"))

    def test_is_valid_ipv6(self):
        self.assertTrue(is_valid_ipv6("::1"))
        self.assertTrue(is_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))
        self.assertFalse(is_valid_ipv6("127.0.0.1"))

    def test_is_private_ip(self):
        self.assertTrue(is_private_ip("192.168.1.1"))
        self.assertTrue(is_private_ip("10.0.0.5"))
        self.assertTrue(is_private_ip("172.16.0.1"))
        self.assertFalse(is_private_ip("8.8.8.8"))

    def test_ip_in_cidr(self):
        self.assertTrue(ip_in_cidr("10.0.1.5", "10.0.0.0/16"))
        self.assertFalse(ip_in_cidr("192.168.1.1", "10.0.0.0/16"))
        self.assertFalse(ip_in_cidr("invalid", "10.0.0.0/16"))

    def test_is_valid_port(self):
        self.assertTrue(is_valid_port(80))
        self.assertTrue(is_valid_port(443))
        self.assertTrue(is_valid_port(65535))
        self.assertFalse(is_valid_port(0))
        self.assertFalse(is_valid_port(70000))
        self.assertFalse(is_valid_port("bad_port"))


if __name__ == "__main__":
    unittest.main()
