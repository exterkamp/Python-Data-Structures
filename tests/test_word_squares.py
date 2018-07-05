import unittest
from algorithms.string.word_squares import word_squares

class TestWordSquares(unittest.TestCase):

    def test_word_squares_basic(self):
        self.assertEqual([['baba', 'abat', 'baba', 'atak']], word_squares(['baba','atak','abat','delt','quad']))

    def test_words_squares_multiple_results(self):
        self.assertEqual([['will', 'idle', 'lliw', 'lewd'], ['will', 'idle', 'llow', 'lewd']], word_squares(['will','idle','lliw','lewd','llow']))

    def test_no_results(self):
        self.assertEqual([], word_squares(['baba','free','quad','high','jill']))