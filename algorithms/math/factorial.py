from functools import reduce

def factorial(n: int):
    """
    Factorial algortihm using dynamic programming.

    Args:
        n: the factorial number to find
    
    Returns:
        The factorial number for n (n!).  Input
        of 0 or less will output 0.
    """
    # base case, reduce must have non-empty list
    if n <= 0:
        return 0
    # use reduce function to multiple elements
    return reduce(lambda x, y: x * y, range(1,n+1))
