import unittest
from structures.heap import Heap

class TestHeap(unittest.TestCase):

    def build_basic_heap(self):
        heap = Heap()

        heap.insert(23)
        heap.insert(12)
        heap.insert(7)
        heap.insert(5)
        heap.insert(34)
        heap.insert(88)
        heap.insert(2)

        return heap

    def test_basic_creation(self):
        heap = self.build_basic_heap()

        self.assertEqual([0,2,7,5,23,34,88, 12], heap.heap_list)

    def test_delete_min(self):
        heap = self.build_basic_heap()

        self.assertEqual(2, heap.delete_min())

        self.assertEqual([0,5,7,12,23,34,88], heap.heap_list)

        heap = Heap()

        self.assertEqual(None, heap.delete_min())

        heap.insert(4)

        self.assertEqual(4, heap.delete_min())

    def test_find_min(self):

        heap = self.build_basic_heap()

        self.assertEqual(2, heap.min())

        self.assertEqual(None, Heap().min())

    def test_build(self):

        built = Heap()

        built.build([23,12,7,5,34,88,2])

        self.assertEqual([0,2,5,7,12,34,88,23], built.heap_list)

    def test_find_min_outside_bounds(self):

        heap = self.build_basic_heap()

        self.assertEqual(None, heap.find_min_child_index(len(heap.heap_list)))

