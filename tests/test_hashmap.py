import unittest
from structures.hash_map import HashMap, djb2, sdbm, lose_lose


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

    def test_djb2(self):

        self.assertEqual(210714636441, djb2('hello'))

        hash_map = HashMap(hash_function=djb2)

        hash_map.insert('hello', 'world')

        self.assertEqual('world',hash_map.get('hello'))

        self.assertEqual([('hello','world')], hash_map.buckets[djb2('hello') % len(hash_map.buckets)])
    
    def test_sdbm(self):
        self.assertEqual(1925877435333486942514, sdbm('hello'))

        hash_map = HashMap(hash_function=sdbm)

        hash_map.insert('hello', 'world')

        self.assertEqual('world', hash_map.get('hello'))

        self.assertEqual([('hello','world')], hash_map.buckets[sdbm('hello') % len(hash_map.buckets)])
    
    def test_lose_lose(self):
        self.assertEqual(532, lose_lose('hello'))

        hash_map = HashMap(hash_function=lose_lose)

        hash_map.insert('hello', 'world')

        self.assertEqual('world', hash_map.get('hello'))

        self.assertEqual([('hello','world')], hash_map.buckets[lose_lose('hello') % len(hash_map.buckets)])