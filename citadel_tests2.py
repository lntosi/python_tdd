import unittest
from citadel3 import Citadel
from rick1 import Rick
from morty1 import Morty


class CitadelTests(unittest.TestCase):
    def test_get_all_residents(self):
        citadel = Citadel()
        residents = citadel.get_all_residents()
        self.assertCountEqual(residents, [])
        
    def test_add_resident(self):
        citadel = Citadel()
        rick = Rick(111)
        morty = Morty(111)
        
        citadel.add_resident(rick)
        citadel.add_resident(morty)
        residents = citadel.get_all_residents()
        
        self.assertEqual(residents[0], rick)
        self.assertEqual(residents[1], morty)
        
if __name__ == '__main__':
    unittest.main()
