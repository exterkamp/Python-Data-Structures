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
    """
    A directed graph represented with an adjacency list.
    """

    def __init__(self, verticies):
        self.graph = defaultdict(list)
        self.verticies = verticies
    
    def add_edge(self, source, destination):
        """
        Add an edge to the graph.

        Add an edge pointing from source vertex
        to destination vertex.

        Args:
            source: the source vertex
            destination: the destination vertex

        """
        self.graph[source].append(destination)

    def topological_sort(self):
        """
        Sort the graph topologically.

        A topological sort lists nodes in such a way
        that every node 's' in 's' -> 'd' directed pairs
        is listed before 'd.'  This will not work in a 
        graph that contains cycles.

        The algorithm looks at every node, and does a
        dfs for each node adjacent to the node and then adds
        the originating node to a stack once all adjacent
        nodes have been searched.  In the end, the stack
        will be in order of a possible topological sort.

        Topological sorts are not necessarily unique.

        Returns:
            A list of vertices in a topological ordering.

        """
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
    