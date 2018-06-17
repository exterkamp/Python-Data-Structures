import unittest
from algorithms.math.first_missing_positive import first_missing_positive

class TestFirstMissingPositive(unittest.TestCase):

    def test_in_order(self):
        self.assertEqual(6,first_missing_positive([1,2,3,4,5]))
        self.assertEqual(6,first_missing_positive([0,1,2,3,4,5]))
    
    def test_with_negatives(self):
        self.assertEqual(7,first_missing_positive([-1,0,-3,6,-5,2,5,3,4,-9,0,1]))
    
    def test_filled_with_zeros(self):
        self.assertEqual(3,first_missing_positive([0,0,0,1,0,0,0,0,0,2,0,0,0,0]))