import unittest
from searches.find_duplicates import duplicates_linear, duplicates_pre_sorted, duplicates_bin_search

class TestFindDuplicates(unittest.TestCase):

    def test_linear(self):
        self.assertEqual([1,2,3], duplicates_linear([1,2,3,4,5,6],[1,2,3,7,8,9]))
        self.assertEqual([4,1,3,2], duplicates_linear([4,5,7,1,9,2,10,3],[4,90,23,1,53,3,2,22]))
    
    def test_pre_sorted(self):
        self.assertEqual([1,2,3], duplicates_pre_sorted([1,2,3,4,5,6],[1,2,3,7,8,9]))
        self.assertNotEqual([1,2,3], duplicates_pre_sorted([5,7,1,9,2,10,3],[4,90,23,1,53,3,2,22]))

    def test_bin_search(self):
        self.assertEqual([1,2,3], duplicates_linear([1,2,3,4,5,6],[1,2,3,7,8,9]))
        self.assertEqual([1,2,3], duplicates_linear([1,2,3,4,5,6],[1,2,3,7,8,9,10,11,12,13,14,15]))
    
    def test_bin_search_second_shorter(self):
        self.assertEqual([1,2,3], duplicates_linear([1,2,3,7,8,9,10,11,12,13,14,15],[1,2,3,4,5,6]))