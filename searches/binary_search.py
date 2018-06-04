def binary_search(list, target):
    """
    Search a sorted list.

    :param list: the input sorted list
    :param target: the value that is to be found
    :return: index of target in list, or -1 if not found
    """
    
    # the initial left and right index
    l = 0
    r = len(list)

    # while left is less than right, if they cross then the value
    # couldn't have been found
    while l <= r:
        
        # get the midpoint of l and r
        mid = (r+l)//2
        
        # if the midpoint is equal to the target, return it
        if list[mid] == target:
            return mid
        # if the mid is greater than target, search the left half
        elif list[mid] > target:
            r = mid - 1
        # if the mid is less than target, search the right half
        else:
            l = mid + 1
    
    # if the target cannot be found, then return -1
    return -1
