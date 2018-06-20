def first_missing_positive(nums):
    """
    Find the first missing positive integer in a list of integers.

    This algorithm sorts the array by making swaps
    and ignoring elements that are greater than the length 
    of the array or negative.

    If the element is equal to the current index (start) then
    it is already in place.  

    If the element is < 0 or > len() or a duplicate, then pull
    in the last element.

    Otherwise swap the current element into place with the
    element that is occupying it's appropriate place. Do this
    until the current value is the correct one for its place or
    the start and end have swapped.

    Args:
        nums: list of integers
    
    Returns:
        The first integer greater than 0 that is not 
        present in the input list.
    """
    start = 0
    end = len(nums) - 1
    while start <= end:
        i = nums[start] - 1
        # if this element is in position
        if i == start:
            start += 1
        # if the element is negative or out of bounds 
        # or a duplicate that is already sorted swap the
        # current element into the oob and dec the end 
        elif i < 0 or i > end or nums[start] == nums[i]:
            nums[start] = nums[end]
            end -= 1
        # swap the element to where it should be
        else:
            nums[start], nums[i] = nums[i], nums[start]
    
    return start + 1