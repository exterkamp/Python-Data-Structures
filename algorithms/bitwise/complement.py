def complement(num):
    """
    Find the non-zero padded binary compelement.

    """
    if not num:
        return 1
    i = 1
    while i <= num:
        num ^= i
        i = i << 1
    return num
