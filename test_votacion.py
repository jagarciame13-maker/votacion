import unittest
from votacion import puede_votar

class TestVotacion(unittest.TestCase):
    def test_puede_votar(self):
        self.assertTrue(puede_votar(20))
        self.assertFalse(puede_votar(16))

if __name__ == "__main__":
    unittest.main()