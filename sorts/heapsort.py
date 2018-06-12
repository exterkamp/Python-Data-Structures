from copy import deepcopy
from heapq import heapify, heappop
from structures.heap import Heap

def heap_sort(lst:list):
    copy_list = deepcopy(lst)
    heapify(copy_list)
    return [heappop(copy_list) for i in range(len(copy_list))]

def max_heap_sort(lst:list):
    copy_list = deepcopy(lst)
    # make all elements negative, so heap is a max heap
    copy_list = list(map(lambda x: x * -1, copy_list))
    heapify(copy_list)
    copy_list = [heappop(copy_list) for i in range(len(copy_list))]
    copy_list =  list(map(lambda x: x * -1, copy_list))
    return copy_list

def custom_heap_sort(lst:list,sort='min'):
    copy_list = deepcopy(lst)
    if sort == 'max':
        copy_list = list(map(lambda x: x * -1, copy_list))
    heap = Heap()
    heap.build(copy_list)
    sorted_list = [heap.delete_min() for i in range(heap.size())]
    if sort == 'max':
        sorted_list = list(map(lambda x: x * -1, sorted_list))
    return sorted_list