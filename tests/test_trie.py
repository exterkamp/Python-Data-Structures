import unittest
from structures.trie import Trie

class TestTrie(unittest.TestCase):

    def test_trie(self):
        trie = Trie(['hello','hel','headway','tree','second','true'])

        self.assertTrue(Trie.eof in trie.head['h']['e']['l'])
        self.assertTrue(Trie.eof in trie.head['t']['r']['e']['e'])
        self.assertTrue(Trie.eof in trie.head['h']['e']['l']['l']['o'])
    
    def test_add(self):
        trie = Trie(['1',])

        with self.assertRaises(KeyError):
            trie.head['2']

        trie.add('2')

        self.assertTrue(Trie.eof in trie.head['2'])