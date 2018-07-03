from collections import defaultdict, deque

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
        self.graph = {}
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
        if len(self.graph) > self.verticies:
            raise IndexError("Too many verticies in graph.")
        
        if source in self.graph:
            self.graph[source].append(destination)
        else:
            self.graph[source] = [destination]
        
        if destination not in self.graph:
            self.graph[destination] = []

    def has_cycle(self):
        """
        Detect if a graph has a cycle.

        Returns:
            True if the graph has a cycle and
            False if the graph is acyclic.

        """

        visited = [0] * self.verticies

        def valid(node):
            # print(visited, node)
            if visited[node] == -1:
                return False
            elif visited[node] == 1:
                return True
            visited[node] = -1
            for neighbor in self.graph[node]:
                if not valid(neighbor):
                    return False
            return True

        for node in range(self.verticies):
            # dfs from each, mark as -1 when visited
            # after dfs set all -1 -> 1
            # cancel if find a 1, as its already been explored
            if not visited[node]:
                # print(visited)
                if valid(node):
                    # set all -1 to 1
                    visited = list(map(lambda x: abs(x),visited))
                else:
                    # cycle!
                    return True
        # no cycle available
        return False

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
        stack = deque()

        def dfs(vertex):
            visited.add(vertex)
            for j in self.graph[vertex]:
                if j not in visited:
                    dfs(j)
            
            stack.appendleft(vertex)

        for key, _ in self.graph.items():
            if key not in visited:
                dfs(key)
        
        return list(stack)

class WeightedGraphNode():

    def __init__(self, val):
        self.val = val
        self.adjacent = {}
    
    def __str__(self):
        return str(self.val) + ' adjacent: ' + str([x for x in self.adjacent])

    def add_adjacent(self, node, weight=0):
        self.adjacent[node] = weight
    
    def remove_adjacent(self, node):
        del self.adjacent[node]

class WeightedGraph():

    def __init__(self):
        self.vertices = {}
    
    def __str__(self):
        return ", ".join([node.__str__() for node in self.vertices.values()])
    
    def add_vertex(self, val):
        vertex = WeightedGraphNode(val)
        self.vertices[val] = vertex
    
    def add_edge(self, src, dst, weight=0):
        if src not in self.vertices:
            self.add_vertex(src)
        if dst not in self.vertices:
            self.add_vertex(dst)
        self.vertices[src].add_adjacent(dst, weight)
    
    def remove_edge(self, src, dst):
        if src not in self.vertices:
            return
        if dst not in self.vertices:
            return
        if dst in self.vertices[src].adjacent:
            self.vertices[src].remove_adjacent(dst)
