import unittest
from structures.lru_cache import LruCache


class LruTests(unittest.TestCase):

    CONST_HELLO = 'hello'

    CONST_WORLD = 'world'

    CONST_HELLO_2 = 'hello 2'

    CONST_BAM = '!'

    def test_LRU_simple(self):
        cache = LruCache(2)

        cache.put(1, self.CONST_HELLO)

        self.assertEqual(cache.get(1), self.CONST_HELLO)

        cache.put(2, self.CONST_WORLD)

        self.assertEqual(cache.get(2), self.CONST_WORLD)

        cache.get(1)

        cache.put(3, self.CONST_BAM)

        self.assertEqual(cache.get(2), -1)

        cache.put(3, self.CONST_BAM)

    def test_LRU_bad_input(self):
        capacity = 0

        self.assertRaises(ValueError, LruCache, capacity)
