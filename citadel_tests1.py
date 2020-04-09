import unittest
from citadel2 import Citadel


class CitadelTests(unittest.TestCase):
    def test_get_all_residents(self):
        citadel = Citadel()
        residents = citadel.get_all_residents()
        self.assertCountEqual(residents, [])
        
if __name__ == '__main__':
    unittest.main()
