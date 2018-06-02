def hamming_distance(x: int, y: int):
    """
    Calculate the number of bits that are different between 2 numbers.

    Args:
        x: first integer to calculate distance on
        Y: second integer to calculate distance on
    
    Returns:
        An integer representing the number of bits that are different
        in the two args.
    """
    # xor numbers to get diff bits as 1's
    xor = x ^ y

    # count the 1's in integer
    return hamming_weight(xor)


def hamming_weight(x: int):
    """
    Count the number of on bits in an integer.

    Args:
        x: the number to count on bits

    Returns:
        Integer representing the number of bits
        that are on (1).
    """
    count = 0
    while x:
        # bitwise AND number with itself minus 1
        x &= x - 1
        count += 1
    return count

