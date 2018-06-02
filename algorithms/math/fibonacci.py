def fibonacci_dp(target: int):
    """
    """
    if target < 1:
        return 0
    # initialize i = 0, and i = 1
    n_minus_1, n = 0, 1
    # start on i = 2 as the first calculated fibb number
    for i in range(2,target+1):
        # calc n and set n_minus_1 to last calc'd value
        n, n_minus_1 = n + n_minus_1, n
    return n

def fibonacci_recursive(target: int):
    """
    """
    # base case of less than 0
    if target <= 0:
        return 0
    # base case of 1
    if target == 1:
        return 1
    # calculate the target number by calculating the previous 2 recursively 
    return fibonacci_recursive(target - 1) + fibonacci_recursive(target - 2)
