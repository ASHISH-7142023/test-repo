import unittest
from src.diffie_hellman import DiffieHellmanParty

class TestDiffieHellman(unittest.TestCase):
    def test_shared_secret_agreement(self):
        alice = DiffieHellmanParty()
        bob = DiffieHellmanParty()

        alice_pub = alice.get_public_key()
        bob_pub = bob.get_public_key()

        alice_secret = alice.compute_shared_secret(bob_pub)
        bob_secret = bob.compute_shared_secret(alice_pub)

        self.assertEqual(alice_secret, bob_secret)

if __name__ == "__main__":
    unittest.main()
