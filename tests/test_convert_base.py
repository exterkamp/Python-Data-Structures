import unittest
from algorithms.math.convert_base import convert_base, convert_digit_to_int

class TestConvertBase(unittest.TestCase):

    def test_convert_digit_valid(self):
        for i in range(10):
            self.assertEqual(i, convert_digit_to_int(str(i)))
        for c,v in [('a',10),('b',11),('c',12),('d',13),('e',14),('f',15)]:
            self.assertEqual(v, convert_digit_to_int(c))
        for c in 'ghijklmnopqrstuvwxyz':
            self.assertEqual(-1, convert_digit_to_int(c))

    def test_convert_base_2(self):
        self.assertEqual(5, convert_base('101',2))
        self.assertEqual(11,convert_base('1011',2))

    def test_convert_base_10(self):
        self.assertEqual(20, convert_base('20',10))
        self.assertEqual(135, convert_base('135',10))
        self.assertEqual(7, convert_base('7',10))
    
    def test_convert_base_16(self):
        self.assertEqual(int('4e',16), convert_base('4e',16))
    
    def test_convert_base_outside_range(self):
        self.assertEqual(-1, convert_base('63',4))
    
    def test_convert_base_invalid_base(self):
        self.assertEqual(-1, convert_base('101',-3))
        self.assertEqual(-1, convert_base('101', 12))