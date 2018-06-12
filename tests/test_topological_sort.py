import unittest
from structures.graph import Graph

class TestGraphTopoSort(unittest.TestCase):

    def test_topological_sort(self):
        graph = Graph(6)
        graph.add_edge(5,2)
        graph.add_edge(5,0)

        graph.add_edge(4,0)
        graph.add_edge(4,1)

        graph.add_edge(2,3)

        graph.add_edge(3,1)

        self.assertEqual([5, 4, 2, 3, 1, 0], graph.topological_sort())



