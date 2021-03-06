import unittest
from algorithms.bitwise.hamming_ops import hamming_distance, hamming_weight

class test_bitwise(unittest.TestCase):

    def test_hamming_weight(self):

        # 5 = 101, hamming weight = 2
        self.assertEqual(hamming_weight(5), 2)

        # 1000 = 1111101000, hamming weight = 6
        self.assertEqual(hamming_weight(1000), 6)
    
    def test_hamming_distance(self):

        # 1 and 10 -> distance = 2
        self.assertEqual(hamming_distance(1,2), 2)

        # 111 and 1101 -> distance = 2
        self.assertEqual(hamming_distance(7, 13), 2)
