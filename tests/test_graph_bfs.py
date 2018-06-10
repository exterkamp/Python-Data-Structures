import unittest
from structures.graph import GraphNode
from searches.breadth_first_search import breadth_first_search_graph

class TestBfsGraph(unittest.TestCase):

    def make_graph(self):
        head = GraphNode(0)
        one = GraphNode(1)
        two = GraphNode(2)
        three = GraphNode(3)
        four = GraphNode(4)

        head.add_adjacent(one)
        head.add_adjacent(two)

        one.add_adjacent(three)

        two.add_adjacent(four)

        four.add_adjacent(two)

        return head
    
    def make_long_graph(self):
        head = GraphNode(0)
        one = GraphNode(1)
        two = GraphNode(2)
        three = GraphNode(3)
        four = GraphNode(4)
        five = GraphNode(5)
        six = GraphNode(6)

        head.add_adjacent(one)
        head.add_adjacent(two)

        one.add_adjacent(three)

        two.add_adjacent(four)

        four.add_adjacent(two)
        four.add_adjacent(five)

        five.add_adjacent(six)

        return head

    def test_basic_graph_bfs(self):
        head = self.make_graph()

        self.assertEqual(3,breadth_first_search_graph(head,3).val)
    
    def test_not_found(self):
        self.assertEqual(None, breadth_first_search_graph(self.make_graph(),8))
    
    def test_with_adjacency_circle(self):
        self.assertEqual(6, breadth_first_search_graph(self.make_long_graph(),6).val)