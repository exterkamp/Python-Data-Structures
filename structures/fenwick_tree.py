class FenwickTree:

    def __init__(self, arr):
        self.nums = [0] * (len(arr)+1)
        self.tree = [0] * (len(arr)+1)

        for i in range(len(arr)):
            self.update(i,arr[i])

    def update(self, index, value):
        index += 1
        delta = value - self.nums[index]
        self.nums[index] = value
        while index <= len(self.tree)-1:
            self.tree[index] += delta
            index += index & (-index)

    def sum_of_n(self, index):
        s = 0
        index += 1

        while index > 0:
            s += self.tree[index]
            index -= index & (-index)

        return s
    
    def sum_of_range(self, start, end):
        # minus 1 from start since the range is (s, e) inclusive on both ends
        start -= 1
        return self.sum_of_n(end) - self.sum_of_n(start)
