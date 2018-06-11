import unittest
from algorithms.bitwise.complement import complement

class TestComplement(unittest.TestCase):

    def test_complement(self):
        self.assertEqual(0b010, complement(0b101))
        self.assertEqual(0b01, complement(0b10))
        self.assertEqual(0b0011000101000001111, complement(0b1100111010111110000))
        self.assertEqual(0b1, complement(0b0))
