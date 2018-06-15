import unittest
from structures.graph import Graph

class TestCycle(unittest.TestCase):

    def test_cycles_true(self):

        graph = Graph(4)

        graph.add_edge(0,1)
        graph.add_edge(1,2)
        graph.add_edge(2,3)
        graph.add_edge(3,0)

        self.assertEqual(True, graph.has_cycle())
    
    def test_cycles_true_complex_graph(self):

        graph = Graph(7)

        graph.add_edge(0,1)
        graph.add_edge(1,2)
        graph.add_edge(3,2)
        graph.add_edge(4,3)
        graph.add_edge(4,6)
        graph.add_edge(5,3)
        graph.add_edge(5,4)
        graph.add_edge(6,5)

        self.assertEqual(True, graph.has_cycle())

    def test_cycles_true_2_node_graph(self):

        graph = Graph(2)

        graph.add_edge(0,1)
        graph.add_edge(1,0)

        self.assertEqual(True, graph.has_cycle())

    def test_cycle_with_discrete_forest(self):

        graph = Graph(6)

        graph.add_edge(0,1)
        graph.add_edge(1,2)
        graph.add_edge(3,4)
        graph.add_edge(4,5)
        graph.add_edge(5,3)

        self.assertEqual(True, graph.has_cycle())


    def test_cycles_false(self):

        graph = Graph(4)

        graph.add_edge(0,1)
        graph.add_edge(1,2)
        graph.add_edge(2,3)

        self.assertEqual(False, graph.has_cycle())