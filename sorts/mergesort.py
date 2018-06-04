def mergesort(list):

    def sort(l):
        
        if len(l) <= 1:
            return l
        
        left = sort(l[:len(l)//2])
        right = sort(l[len(l)//2:])

        output = merge(left, right)
        # print('->' + str(output))
        return output
    
    def merge(l1, l2):
        # print(l1,l2)
        res = []

        while l1 and l2:
            if l1[0] < l2[0]:
                res.append(l1.pop(0))
            else:
                res.append(l2.pop(0))
        while l1:
            res.append(l1.pop(0))
        while l2:
            res.append(l2.pop(0))
        return res

    return sort(list)
