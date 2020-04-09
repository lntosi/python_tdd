import unittest
from morty1 import Morty


class MortyTests(unittest.TestCase):
    def test_universe(self):
        morty = Morty(111)
        self.assertEqual(morty.universe, 111)
        
if __name__ == '__main__':
    unittest.main()
