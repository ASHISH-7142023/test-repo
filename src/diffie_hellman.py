"""Diffie-Hellman Key Exchange protocol simulation."""

import secrets

PRIME_1024 = int(
    "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1"
    "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"
    "EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245"
    "E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED"
    "EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381"
    "FFFFFFFFFFFFFFFF", 16
)
GENERATOR = 2


class DiffieHellmanParty:
    """Represents a participant in a Diffie-Hellman key exchange."""

    def __init__(self, p: int = PRIME_1024, g: int = GENERATOR):
        self.p = p
        self.g = g
        self._private_key = secrets.randbelow(self.p - 2) + 2

    def get_public_key(self) -> int:
        """Compute public key g^private mod p."""
        return pow(self.g, self._private_key, self.p)

    def compute_shared_secret(self, peer_public_key: int) -> int:
        """Compute shared secret peer_public^private mod p."""
        if not (1 < peer_public_key < self.p - 1):
            raise ValueError("Invalid peer public key.")
        return pow(peer_public_key, self._private_key, self.p)
