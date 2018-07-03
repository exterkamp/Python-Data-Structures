from collections import deque

def mergesort(list):

    def sort(l):
        
        if len(l) <= 1:
            return l
        
        left = sort(l[:len(l)//2])
        right = sort(l[len(l)//2:])

        output = merge(left, right)
        
        return output
    
    def merge(l1, l2):

        res = []
        l1 = deque(l1)
        l2 = deque(l2)

        while l1 and l2:
            if l1[0] < l2[0]:
                res.append(l1.popleft())
            else:
                res.append(l2.popleft())
        while l1:
            res.append(l1.popleft())
        while l2:
            res.append(l2.popleft())
        return res

    return sort(list)
