from collections import defaultdict

class GraphNode():

    def __init__(self, val):
        self.val = val
        self.adjacent_list = set()
    
    def add_adjacent(self, node):
        self.adjacent_list.add(node)
    
    def remove_adjacent(self, node):
        self.adjacent_list.remove(node)

class Graph():

    def __init__(self, verticies):
        self.graph = defaultdict(list)
        self.verticies = verticies
    
    def add_edge(self, source, destination):
        self.graph[source].append(destination)

    def topological_sort(self):
        visited = set()
        stack = []

        def dfs(vertex):
            visited.add(vertex)
            for i in self.graph[vertex]:
                if i not in visited:
                    dfs(i)
            
            stack.insert(0, vertex)
        
        for i in range(self.verticies):
            if i not in visited:
                dfs(i)
        
        return stack
    