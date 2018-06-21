import unittest
from structures.graph import WeightedGraphNode, WeightedGraph

class TestWeightedGraph(unittest.TestCase):

    def test_add_vertex(self):

        graph = WeightedGraph()

        graph.add_vertex('a')
        graph.add_vertex('b')
        graph.add_vertex('c')

        self.assertEqual(['a','b','c'], list(graph.vertices.keys()))
    
    def test_add_edge(self):

        graph = WeightedGraph()

        graph.add_edge('a','b',1)
        graph.add_edge('a','c',3)
        graph.add_edge('b','c',2)

        self.assertEqual({'b':1,'c':3}, graph.vertices['a'].adjacent)

        self.assertEqual({'c':2}, graph.vertices['b'].adjacent)

    def test_remove_adjacent(self):

        graph = WeightedGraph()

        graph.add_edge('a','b',2)

        graph.remove_edge('a','b')

        graph.remove_edge('a','c')

        graph.remove_edge('c','a')

        self.assertEqual({}, graph.vertices['a'].adjacent)

    def test_print_graph(self):
        graph = WeightedGraph()

        graph.add_edge('a','b',1)
        graph.add_edge('a','c',3)
        graph.add_edge('b','c',2)

        self.assertEqual("a adjacent: ['b', 'c'], b adjacent: ['c'], c adjacent: []", graph.__str__())