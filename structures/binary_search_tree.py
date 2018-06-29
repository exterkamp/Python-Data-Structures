from structures.tree_node import BinaryTreeNode

class BinarySearchTree():

    def __init__(self):
        self.head = None
    
    def insert(self, val):
        if not self.head:
            self.head = BinaryTreeNode(val, None)
            return
        def add_node_recursive(node):
            if val < node.value:
                if node.left:
                    add_node_recursive(node.left)
                else:
                    node.left = BinaryTreeNode(val, node)
            else:
                if node.right:
                    add_node_recursive(node.right)
                else:
                    node.right = BinaryTreeNode(val, node)
        add_node_recursive(self.head)
    
    def min(self):
        return self.head.min().value

    def delete(self, value):
        self.head.delete(value)

    def search(self, value):
        node = self.head
        while node:
            if value == node.value:
                return node
            if value > node.value:
                node = node.right
            else:
                node = node.left
        # return None if not found
        return node

    def in_order_traversal(self):
        output = []
        def recur(node):
            if node:
                recur(node.left)
                output.append(node.value)
                recur(node.right)
        recur(self.head)
        return output

    def merge(self, tree):

        def mergeOntoT1(t1, t2):
            if not t1:
                return t2
            if not t2:
                return t1
            
            t1.value += t2.value
            
            # look left
            t1.left = mergeOntoT1(t1.left, t2.left)
            
            # look right
            t1.right = mergeOntoT1(t1.right, t2.right)
            
            return t1
        
        mergeOntoT1(self.head, tree.head)