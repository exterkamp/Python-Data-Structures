from searches.binary_search import binary_search

def duplicates_linear(arr1, arr2):
    arr1_seen = set(arr1)
    output = []

    for element in arr2:
        if element in arr1_seen:
            output.append(element)

    return output

def duplicates_pre_sorted(arr1, arr2):
    output = []
  
    ptr_1 = 0
    ptr_2 = 0
    
    while ptr_1 < len(arr1) and ptr_2 < len(arr2):
        
        if arr2[ptr_2] == arr1[ptr_1]:
            output.append(arr1[ptr_1])
            ptr_1 += 1
            ptr_2 += 1
        elif arr2[ptr_2] > arr1[ptr_1]:
            ptr_1 += 1
        else:
            ptr_2 += 1
    
    return output

def duplicates_bin_search(arr1, arr2):
    """
    Find duplicates in 2 sets, where one is much larger than the other.

    """

    # if arr1 is greater, swap them
    if len(arr2) < len(arr1):
        arr1, arr2 = arr2, arr1
    
    output = []

    for element in arr1:
        if binary_search(arr2, element) > 0:
            output.append(element)

    return output
