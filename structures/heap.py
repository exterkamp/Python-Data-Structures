class Heap():

    def __init__(self):
        self.heap_list = [0]

    def insert(self, value: int):
        self.heap_list.append(value)
        self.percolate(self.size())

    def percolate(self, i):
        while i // 2 > 0:
            parent = i // 2
            if self.heap_list[i] < self.heap_list[parent]:
                self.heap_list[i], self.heap_list[parent] = self.heap_list[parent], self.heap_list[i]
            i = i // 2
    
    def sift(self, i):
        while (i * 2) <= self.size():
            mc_i = self.find_min_child_index(i)
            if self.heap_list[i] > self.heap_list[mc_i]:
                self.heap_list[i], self.heap_list[mc_i] = self.heap_list[mc_i], self.heap_list[i]
            i = mc_i
    
    def find_min_child_index(self, i):
        if (i * 2) > self.size():
            return None
        if (i * 2) + 1 > self.size():
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def min(self):
        if len(self.heap_list) > 1:
            return self.heap_list[1]
        else:
            return None

    def delete_min(self):
        if self.size() == 0:
            return None
        if self.size() == 1:
            return self.heap_list.pop()
        
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list.pop()
        self.sift(1)
        return min_val

    def build(self, lst:list):
        i = len(lst) // 2
        self.heap_list = [0] + lst
        while i > 0:
            self.sift(i)
            i -= 1

    def size(self):
        return len(self.heap_list) - 1
