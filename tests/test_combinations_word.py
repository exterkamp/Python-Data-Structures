import unittest
from algorithms.string.combinations import combinations_of_word

class TestCombinationsWord(unittest.TestCase):

    def test_combinations(self):
        self.assertEqual(['t', 'tw', 'two', 'w', 'wo', 'o'], combinations_of_word('two'))
        self.assertEqual(['1', '12', '123', '1234', '2', '23', '234', '3', '34', '4'], combinations_of_word('1234'))
