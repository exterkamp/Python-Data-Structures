import unittest
from structures.binary_search_tree import BinarySearchTree
from structures.tree_node import BinaryTreeNode


class TreeTests(unittest.TestCase):

    def make_simple_tree(self):
        tree = BinarySearchTree()

        tree.insert(12)
        tree.insert(7)
        tree.insert(3)
        tree.insert(18)
        tree.insert(32)
        tree.insert(1)
        tree.insert(5)

        return tree
    
    def test_pre_order_traversal(self):
        
        tree = self.make_simple_tree()

        self.assertEqual([1,3,5,7,12,18,32], tree.in_order_traversal())

    def test_min(self):

        tree = self.make_simple_tree()

        self.assertEqual(1, tree.min())

    def test_delete(self):

        tree = self.make_simple_tree()

        tree.delete(1) # delete node that has no children

        self.assertEqual([3,5,7,12,18,32], tree.in_order_traversal())

        tree.delete(18) # delete node that has 1 child, right

        self.assertEqual([3,5,7,12,32], tree.in_order_traversal())

        tree.insert(15)

        tree.delete(32) # delete node that has 1 child, left

        self.assertEqual([3,5,7,12,15], tree.in_order_traversal())

        tree.insert(8)

        tree.delete(7) # delete node that has 2 children

        self.assertEqual([3,5,8,12,15], tree.in_order_traversal())

        # miss on the delete
        tree.delete(9)

    def test_search(self):

        tree = self.make_simple_tree()

        self.assertEqual(12, tree.search(12).value)

        self.assertEqual(None, tree.search(87))

        self.assertEqual(3, tree.search(3).value)

    def test_merge(self):

        tree = self.make_simple_tree()

        tree2 = BinarySearchTree()

        tree2.insert(5)
        tree2.insert(9)
        tree2.insert(10)

        tree.merge(tree2)

        self.assertEqual(17, tree.head.value)
        self.assertEqual(27, tree.search(27).value)
        self.assertEqual(42, tree.search(42).value)