class BinaryTreeNode():

    def __init__(self, value, parent):
        self.left = None
        self.right = None
        self.value = value
        self.parent = parent

    def min(self):
        node = self
        while node.left:
            node = node.left
        return node      

    def replace_self_in_parent(self, new_node):
        if self.parent:
            if self is self.parent.left:
                self.parent.left = new_node
            else:
                self.parent.right = new_node
        
        if new_node:
            new_node.parent = self.parent
    
    def delete(self, value):
        if value > self.value:
            if self.right:
                self.right.delete(value)
            return
        elif value < self.value:
            if self.left:
                self.left.delete(value)
            return 
        if self.left and self.right:
            successor = self.right.min()
            self.value = successor.value
            successor.delete(successor.value)
        elif self.left:
            self.replace_self_in_parent(self.left)
        elif self.right:
            self.replace_self_in_parent(self.right)
        else:
            self.replace_self_in_parent(None)
