def quicksort(ar:list):
    """
    Sort a list with quicksort algorithm.

    The quicksort algorithm splits a list into
    two parts and recursively sorts those parts
    by making swaps based on the elements value
    in relation to the pivot value.  It is an 
    O(n log(n)) sort.

    Args:
        ar: list to sort.

    Returns:
        The input list sorted.
    """
    def sort(ar, lo, hi):
        # if the two ends haven't swapped
        if lo < hi:
            # find the partition
            partition_index = partition(ar, lo, hi)
            # sort both sides
            sort(ar, lo, partition_index - 1)
            sort(ar, partition_index + 1, hi)
    
    def partition(ar, lo, hi):
        # basic partition by using the high value as a pivot
        pivot = ar[hi]

        # the value being examined 
        i = lo
        for j in range(lo, hi):
            # 
            if ar[j] <= pivot:
                ar[i], ar[j] = ar[j], ar[i]
                i += 1
        # swap the pivot into place
        ar[i], ar[hi] = ar[hi], ar[i]

        return i
    
    sort(ar, 0, len(ar)-1)

    return ar