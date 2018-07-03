import unittest
from structures.graph import Graph

class TestCycle(unittest.TestCase):

    def test_non_int(self):

        graph = Graph(4)

        graph.add_edge('Tampa','Colorado')
        graph.add_edge('Colorado','Las Vegas')
        graph.add_edge('Las Vegas', 'Seattle')
        graph.add_edge('Seattle','Anchorage')

        self.assertEqual(['Tampa', 'Colorado', 'Las Vegas', 'Seattle', 'Anchorage'], graph.topological_sort())

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

    def test_too_many_verticies_error(self):

        graph = Graph(1)

        graph.add_edge(0,1)
        with self.assertRaises(IndexError):
            graph.add_edge(1,2)