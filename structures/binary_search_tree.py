from structures.tree_node import BinaryTreeNode

class BinarySearchTree():

    def __init__(self):
        self.head = None
    
    def add_node(self, val):
        if not self.head:
            self.head = BinaryTreeNode(val)
            return
        def add_node_recursive(node):
            if val < node.value:
                if node.left:
                    add_node_recursive(node.left)
                else:
                    node.left = BinaryTreeNode(val)
            else:
                if node.right:
                    add_node_recursive(node.right)
                else:
                    node.right = BinaryTreeNode(val)
        add_node_recursive(self.head)
    
    def in_order_traversal(self):
        output = []
        def recur(node):
            if node:
                recur(node.left)
                output.append(node.value)
                recur(node.right)
        recur(self.head)
        return output
