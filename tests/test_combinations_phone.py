import unittest
from algorithms.string.combinations import combinations_of_phone_input

class TestCombinationsPhone(unittest.TestCase):

    def test_phone_combo_simple(self):
        self.assertEqual(['da', 'db', 'dc', 'ea', 'eb', 'ec', 'fa', 'fb', 'fc'], combinations_of_phone_input('32'))