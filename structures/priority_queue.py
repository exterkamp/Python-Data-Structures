import itertools
from heapq import heappush, heappop

class PriorityQueue():

    pq = []
    mapper = {}
    REMOVED = '__removed-task__'
    counter = itertools.count()

    def __init__(self):
        pass
    
    def add_task(self, task, priority=0):
        if task in self.mapper:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.mapper[task] = entry
        heappush(self.pq, entry)
    
    def remove_task(self, task):
        entry = self.mapper.pop(task)
        entry[-1] = self.REMOVED
    
    def set_priority(self, task, priority=None):
        if task in self.mapper:
            entry = self.mapper.pop(task)

            if not priority:
                priority = min(0, entry[0] - 1)

            self.add_task(entry[2], priority)

    def pop_task(self):
        while self.pq:
            _, _, task = heappop(self.pq)
            if task is not self.REMOVED:
                del self.mapper[task]
                return task
        raise KeyError('Pop from empty priority queue.')
