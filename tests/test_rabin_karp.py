import unittest
from algorithms.string.rabin_karp_substring_search import rabin_karp_find_substring

class TestRabinKarp(unittest.TestCase):

    def test_rabin_karp(self):
        self.assertEqual(2, rabin_karp_find_substring('hello','llo'))
        self.assertEqual(5, rabin_karp_find_substring('aabbababaa','babaa'))
    
    def test_rabin_karp_miss(self):
        self.assertEqual(-1, rabin_karp_find_substring('hello','af'))

    def test_find_first_with_mult(self):
        self.assertEqual(3, rabin_karp_find_substring('abcabbabcabb', 'abb'))
    
    def test_same_hash_diff_order(self):
        self.assertEqual(15, rabin_karp_find_substring('Where are your ears?', 'ear', base=0))