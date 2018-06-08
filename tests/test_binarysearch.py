import unittest
from searches.binary_search import binary_search

class test_binary_search(unittest.TestCase):

    sorted_list = [2, 3, 4, 7, 8, 9, 12, 20, 24, 39, 84, 99]

    unsorted_list = [7, 9, 3, 24, 84, 12, 4, 20, 39, 8, 2, 99]

    def test_binary_search(self):
        self.assertEqual(binary_search(self.sorted_list, 9), 5)
    
    def test_binary_search_not_found(self):
        self.assertEqual(binary_search(self.sorted_list, 10), -1)
    
    def test_binary_search_not_sorted(self):
        self.assertEqual(binary_search(self.unsorted_list, 20), -1)
