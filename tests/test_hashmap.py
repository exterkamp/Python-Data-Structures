import unittest
from structures.hash_map import HashMap


class TestHashMap(unittest.TestCase):

    def test_insert(self):
        hash_map = HashMap()

        hash_map.insert('hello', 'world')

        self.assertEqual('world', hash_map.get('hello'))

    def test_get(self):
        hash_map = HashMap()

        hash_map.insert(3, 'three')
        hash_map.insert('99', 99)

        self.assertEqual('three', hash_map.get(3))

        self.assertEqual(99, hash_map.get('99'))

    def test_collisions(self):
        hash_map = HashMap()

        for i in range(257):
            hash_map.insert(i, str(i))
        
        for i in range(257):
            self.assertEqual(str(i), hash_map.get(i))

    def test_overwrite(self):
        hash_map = HashMap()

        hash_map.insert(1, '1')

        self.assertEqual('1', hash_map.get(1))

        hash_map.insert(1, '2')

        self.assertEqual('2', hash_map.get(1))

    def test_not_found(self):
        hash_map = HashMap()

        with self.assertRaises(KeyError):
            hash_map.get(1)

    def test_delete(self):
        hash_map = HashMap()

        hash_map.insert(1, '1')

        self.assertEqual('1', hash_map.get(1))

        self.assertEqual((1,'1'), hash_map.delete(1))

        with self.assertRaises(KeyError):
            hash_map.get(1)
        
        with self.assertRaises(KeyError):
            hash_map.delete(1)
