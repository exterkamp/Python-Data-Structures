import unittest
from structures.naive_tree import NaiveBinaryTree
from structures.tree_node import BinaryTreeNode


class TreeTests(unittest.TestCase):

    def make_simple_tree(self):
        tree = NaiveBinaryTree()

        tree.head = BinaryTreeNode(3, None)

        tree.head.left = BinaryTreeNode(5, tree.head)

        tree.head.right = BinaryTreeNode(7, tree.head)

        return tree
    
    def make_complex_tree(self):
        tree = NaiveBinaryTree()

        tree.head = BinaryTreeNode(12, None)

        tree.head.left = BinaryTreeNode(3, tree.head)

        tree.head.right = BinaryTreeNode(6, tree.head)

        tree.head.left.right = BinaryTreeNode(8, tree.head.left)

        tree.head.right.right = BinaryTreeNode(2, tree.head.right)

        tree.head.left.right.right = BinaryTreeNode(17, tree.head.left.right)

        return tree
    
    def test_pre_order_traversal(self):
        
        tree = self.make_simple_tree()

        self.assertEqual([3,5,7], tree.pre_order_traversal())

        tree = self.make_complex_tree()

        self.assertEqual([12,3,8,17,6,2], tree.pre_order_traversal())

    def test_in_order_traversal(self):
        
        tree = self.make_simple_tree()

        self.assertEqual([5,3,7], tree.in_order_traversal())

        tree = self.make_complex_tree()

        self.assertEqual([3,8,17,12,6,2], tree.in_order_traversal())
    
    def test_post_order_traversal(self):
        
        tree = self.make_simple_tree()

        self.assertEqual([5,7,3], tree.post_order_traversal())

        tree = self.make_complex_tree()

        self.assertEqual([17,8,3,2,6,12], tree.post_order_traversal())

    def test_level_oreder_traversal(self):

        tree = self.make_simple_tree()

        self.assertEqual([3, 5, 7], tree.level_order_traversal())

        tree = self.make_complex_tree()

        self.assertEqual([12,3,6,8,2,17], tree.level_order_traversal())

    def test_print(self):
        
        tree = self.make_simple_tree()
        
        self.assertEqual('[3, 5, 7]', tree.__str__())
