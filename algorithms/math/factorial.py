def factorial(n: int):
    """
    Factorial algortihm using dynamic programming.
    """
    i = 1
    fact = 1
    while i <= n:
        fact *= i
        i += 1
    return fact

