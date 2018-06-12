class GraphNode():

    def __init__(self, val):
        self.val = val
        self.adjacent_list = set()
    
    def add_adjacent(self, node):
        self.adjacent_list.add(node)
    
    def remove_adjacent(self, node):
        self.adjacent_list.remove(node)
