import unittest
from structures.binary_search_tree import BinarySearchTree
from structures.tree_node import BinaryTreeNode


class TreeTests(unittest.TestCase):

    def make_simple_tree(self):
        tree = BinarySearchTree()

        tree.add_node(12)
        tree.add_node(7)
        tree.add_node(3)
        tree.add_node(18)
        tree.add_node(32)
        tree.add_node(1)
        tree.add_node(5)

        return tree
    
    def test_pre_order_traversal(self):
        
        tree = self.make_simple_tree()

        self.assertEqual([1,3,5,7,12,18,32], tree.in_order_traversal())

if __name__ == '__main__':
    unittest.main()
