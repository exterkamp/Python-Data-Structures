import unittest
from algorithms.string.permutations import permutations_of_word

class TestPermuteWord(unittest.TestCase):

    def test_permutation_word(self):
        self.assertEqual(['two', 'tow', 'wto', 'wot', 'otw', 'owt'], permutations_of_word('two'))
        self.assertEqual(['123', '132', '213', '231', '312', '321'], permutations_of_word('123'))