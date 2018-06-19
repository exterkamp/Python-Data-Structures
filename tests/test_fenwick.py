import unittest
from structures.fenwick_tree import FenwickTree

class TestFenwickTree(unittest.TestCase):

    def test_basic_sum(self):
        lst = [1,5,7,6,4]
        sums = [1,6,13,19,23]
        tree = FenwickTree(lst)

        for i in range(len(lst)):
            self.assertEqual(sums[i],tree.sum_of_n(i))

    def test_sum_range(self):
        lst = [1,3,8,2,10,6]

        tree = FenwickTree(lst)

        self.assertEqual(11,tree.sum_of_range(1,2))
        self.assertEqual(20,tree.sum_of_range(2,4))
        self.assertEqual(30,tree.sum_of_range(0,5))
    
    def test_modified_tree(self):
        lst = [1,2,3,4,5]
        sums = [1,3,6,10,15]

        tree = FenwickTree(lst)

        for i in range(len(lst)):
            self.assertEqual(sums[i],tree.sum_of_n(i))

        tree.update(1,10)
        tree.update(3,1)

        sums = [1,11,14,15,20]

        for i in range(len(lst)):
            self.assertEqual(sums[i],tree.sum_of_n(i))
