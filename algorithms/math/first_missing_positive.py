def first_missing_positive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    start = 0
    end = len(nums) - 1
    while start <= end:
        i = nums[start] -1
        if i == start:
            start += 1
        elif i < 0 or i > end or nums[start] == nums[i]:
            nums[start] = nums[end]
            end -= 1
        else:
            nums[start] = nums[i]
            nums[i] = i + 1
    return start + 1