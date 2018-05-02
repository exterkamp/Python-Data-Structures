class Mergesort:

    def recursive_sort(list):

        def merge_sort(l):
            
            if len(l) <= 1:
                return l
            
            left = merge_sort(l[:len(l)//2])
            right = merge_sort(l[len(l)//2:])

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

        return merge_sort(list)

    recursive_sort = staticmethod(recursive_sort)
