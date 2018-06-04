def radixsort(ar: list, base=10):
    """
    """
    def create_buckets(ar, iteration):
        buckets = [[] for x in range(0,base)]

        for num in ar:
            digit = (num // (base ** iteration)) % base
            buckets[digit].append(num)

        return buckets

    def create_list(buckets):
        nums = []
        for bucket in buckets:
            for num in bucket:
                nums.append(num)
        return nums

    max_value = max(ar)
    
    iteration = 0

    while base ** iteration <= max_value:
        ar = create_list(create_buckets(ar,iteration))
        iteration += 1
    
    return ar




