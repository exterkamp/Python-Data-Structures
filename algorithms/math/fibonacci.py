def fibonacci_dp(target: int):
    """
    Fibonacci found with dynamic programming.

    Fibonacci found with only keeping track of
    the previous 2 numbers.  O(n) runtime complexity.

    Args:
        target: the fibonacci number to find

    Returns:
        The nth fibonacci number.
    """
    if target < 1:
        return 0
    # initialize i = 0, and i = 1
    n_minus_1, n = 0, 1
    # start on i = 2 as the first calculated fibb number
    for _ in range(2,target+1):
        # calc n and set n_minus_1 to last calc'd value
        n, n_minus_1 = n + n_minus_1, n
    return n

def fibonacci_recursive(target: int):
    """
    Fibonacci found with recursion.

    Fibonacci found with recursive algortihm.
    O(2^n) runtime complexity.

    Args:
        target: the fibonacci number to find

    Returns:
        The nth fibonacci number.
    """
    # base case of 0 or 1, return 0 or 1.  If less than 0, ceil to 0.
    if target <= 1:
        return max(0, target)
    # calculate the target number by calculating the previous 2 recursively 
    return fibonacci_recursive(target - 1) + fibonacci_recursive(target - 2)
