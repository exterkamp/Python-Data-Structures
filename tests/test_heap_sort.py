import unittest
from sorts.heapsort import heap_sort, max_heap_sort, custom_heap_sort

class TestHeapSort(unittest.TestCase):

    random_list = [7, 9, 3, 24, 84, 12, 3, 4, 20, 39, 8, 2, 4, 99, 24, 4]

    sorted_list = [2, 3, 3, 4, 4, 4, 7, 8, 9, 12, 20, 24, 24, 39, 84, 99]

    def test_heap_sort(self):
        self.assertEqual(self.sorted_list, heap_sort(self.random_list))

    def test_max_heap_sort(self):
        self.assertEqual(self.sorted_list[::-1], max_heap_sort(self.random_list))
    
    def test_heap_sort_custom(self):
        self.assertEqual(self.sorted_list, custom_heap_sort(self.random_list))
    
    def test_heap_max_sort_custom(self):
        self.assertEqual(self.sorted_list[::-1], custom_heap_sort(self.random_list, 'max'))