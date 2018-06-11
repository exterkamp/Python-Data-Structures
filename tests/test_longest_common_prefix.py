import unittest
from algorithms.string.longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

class TestLongestCommonPrefix(unittest.TestCase):

    def test_lcp(self):
        self.assertEqual('he', find_longest_common_prefix(['hello','hellieo','he']))
        self.assertEqual('he', find_longest_common_prefix_reduce(['hello','hellieo','he']))
    
    def test_lcp_empty(self):
        self.assertEqual('', find_longest_common_prefix([]))
        self.assertEqual('', find_longest_common_prefix_reduce([]))
    
    def test_lcp_no_prefix(self):
        self.assertEqual('', find_longest_common_prefix(['fcp','jpl','the','first']))
        self.assertEqual('', find_longest_common_prefix_reduce(['fcp','jpl','the','first']))
    
    def test_lcp_full_prefix(self):
        self.assertEqual('full', find_longest_common_prefix(['full','full','full']))
        self.assertEqual('full', find_longest_common_prefix_reduce(['full','full','full']))
