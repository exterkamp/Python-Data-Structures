from collections import deque

class NaiveBinaryTree():

    def __init__(self):
        self.head = None
    
    def __str__(self):
        """
        Print a pre order traversal.
        """
        output = self.pre_order_traversal()
        str_output =  '[' + ", ".join(map(str, output)) + ']'
        return str_output
    
    def pre_order_traversal(self):
        output = []
        def recur(node):
            if node:
                output.append(node.value)
                recur(node.left)
                recur(node.right)
        recur(self.head)
        return output
    
    def in_order_traversal(self):
        output = []
        def recur(node):
            if node:
                recur(node.left)
                output.append(node.value)
                recur(node.right)
        recur(self.head)
        return output
    
    def post_order_traversal(self):
        output = []
        def recur(node):
            if node:
                recur(node.left)
                recur(node.right)
                output.append(node.value)
        recur(self.head)
        return output

    def level_order_traversal(self):
        output = []
        queue = deque([self.head])

        while queue:
            output.extend(list(map(lambda n: n.value, list(queue))))
            next_level = deque()
            while queue:
                current = queue.popleft()
                if current.left:
                    next_level.append(current.left)
                if current.right:
                    next_level.append(current.right)
            queue = next_level
        return output
