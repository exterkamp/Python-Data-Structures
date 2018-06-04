import unittest
from algorithms.math.factorial import factorial
from algorithms.math.fibonacci import fibonacci_dp, fibonacci_recursive

class test_math(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(0), 0)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_fibonacci_dp(self):
        self.assertEqual(fibonacci_dp(-1), 0)
        self.assertEqual(fibonacci_dp(0), 0)
        self.assertEqual(fibonacci_dp(1), 1)
        self.assertEqual(fibonacci_dp(5), 5)
        self.assertEqual(fibonacci_dp(12), 144)
    
    def test_fibonacci_recursive(self):
        self.assertEqual(fibonacci_recursive(-1), 0)
        self.assertEqual(fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci_recursive(1), 1)
        self.assertEqual(fibonacci_recursive(5), 5)
        self.assertEqual(fibonacci_recursive(12), 144)

if __name__ == '__main__':
    unittest.main()
