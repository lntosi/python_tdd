import unittest
from rick2 import Rick
from morty2 import Morty


class RickTests(unittest.TestCase):
    def test_universe(self):
        rick = Rick(111)
        self.assertEqual(rick.universe, 111)
        
    def test_has_morty(self):
        rick = Rick(111)
        self.assertEqual(rick.morty, None)
        
if __name__ == '__main__':
    unittest.main()
