import unittest
from algorithms.math.factorial import factorial
from algorithms.math.fibonacci import fibonacci_dp, fibonacci_recursive

class test_math(unittest.TestCase):

    def test_factorial(self):
        self.assertEquals(factorial(0), 0)
        self.assertEquals(factorial(1), 1)
        self.assertEquals(factorial(3), 6)
        self.assertEquals(factorial(5), 120)
        self.assertEquals(factorial(10), 3628800)

    def test_fibonacci_dp(self):
        self.assertEquals(fibonacci_dp(-1), 0)
        self.assertEquals(fibonacci_dp(0), 0)
        self.assertEquals(fibonacci_dp(1), 1)
        self.assertEquals(fibonacci_dp(5), 5)
        self.assertEquals(fibonacci_dp(12), 144)
    
    def test_fibonacci_recursive(self):
        self.assertEquals(fibonacci_recursive(-1), 0)
        self.assertEquals(fibonacci_recursive(0), 0)
        self.assertEquals(fibonacci_recursive(1), 1)
        self.assertEquals(fibonacci_recursive(5), 5)
        self.assertEquals(fibonacci_recursive(12), 144)

if __name__ == '__main__':
    unittest.main()
