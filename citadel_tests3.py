import unittest
from citadel3 import Citadel
from rick4 import Rick
from morty2 import Morty


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
        
    def test_picle_ricks_with_morties(self):
        citadel = Citadel()
        rick = Rick(111)
        morty = Morty(111)
        rick.assign(morty)
        
        citadel.add_resident(rick)
        citadel.add_resident(morty)
        
        citadel.picle_ricks_with_morties()
        residents = citadel.get_all_residents()
        
        self.assertTrue(residents[0].is_pickle)
        
if __name__ == '__main__':
    unittest.main()
