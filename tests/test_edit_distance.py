import unittest
from algorithms.string.edit_distance import calculate_edit_distance

class TestEditDistance(unittest.TestCase):

    def test_edit_distance(self):

        self.assertEqual(['Substitute h', 'Insert l', 'Substitute l'], calculate_edit_distance('hello','teio'))

