import unittest
from sorts.mergesort import mergesort


class test_mergesort_methods(unittest.TestCase):

    random_list = [7, 9, 3, 24, 84, 12, 3, 4, 20, 39, 8, 2, 4, 99, 24, 4]

    sorted_list = [2, 3, 3, 4, 4, 4, 7, 8, 9, 12, 20, 24, 24, 39, 84, 99]

    def test_mergesort(self):
        self.assertEqual(mergesort(self.random_list), self.sorted_list)
