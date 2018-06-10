import unittest
from structures.graph import GraphNode

class TestGraph(unittest.TestCase):

    def test_graph_node(self):
        self.assertEqual(4,GraphNode(4).val)
    
    def test_insert(self):
        node = GraphNode(1)

        two = GraphNode(2)
        three = GraphNode(3)
        node.add_adjacent(two)

        self.assertTrue(two in node.adjacent_list)

        self.assertFalse(three in node.adjacent_list)

        three.add_adjacent(three)

        self.assertTrue(two in node.adjacent_list)

    def test_delete(self):
        node = GraphNode(1)
        two = GraphNode(2)
        node.add_adjacent(two)

        node.remove_adjacent(two)
        
        self.assertTrue(two not in node.adjacent_list)

        with self.assertRaises(KeyError):
            node.remove_adjacent(GraphNode(1))
