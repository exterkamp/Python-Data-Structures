import unittest
from searches.breadth_first_search import breadth_first_search

class TestBFS(unittest.TestCase):

    def make_simple_grid(self):
        return [
            [1,0,3,4],
            [5,6,2,6],
            [8,8,1,3],
        ]
    
    def make_complex_grid(self):
        return [
            [1,0,3,4,7,12,4,111],
            [5,6,2,6,0,1,54,3],
            [8,8,1,3,2,6,8,22],
            [8,8,1,3,4,0,77,1],
            [8,8,1,3,-1,4,2,9],
        ]

    def test_bfs_basic(self):
        self.assertEqual((1,2), breadth_first_search(self.make_simple_grid(), (3, 0), 8))

        self.assertEqual((3,2), breadth_first_search(self.make_simple_grid(), (0, 2), 3))

        self.assertEqual((2,0), breadth_first_search(self.make_simple_grid(), (0, 0), 3))
    
    def test_bfs_complex(self):
        self.assertEqual((7,0), breadth_first_search(self.make_complex_grid(), (7, 4), 111))

        self.assertEqual((0,4), breadth_first_search(self.make_complex_grid(), (0, 4), 8))

    def test_bfs_empty(self):
        self.assertEqual(None, breadth_first_search([],(0,1),0))
    
    def test_bfs_not_found(self):
        self.assertEqual(None, breadth_first_search(self.make_simple_grid(), (0,0), -1))