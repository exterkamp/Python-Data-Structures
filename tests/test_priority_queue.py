import unittest
from structures.priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def test_pq_simple(self):
        pq = PriorityQueue()
        pq.add_task('drive to work', 2)
        pq.add_task('get keys')
        pq.add_task('load car', 1)
        pq.add_task('check gas', 1)
        pq.add_task('turn on car', 1)
        pq.add_task('park at work', 3)
        pq.remove_task('load car')
        pq.add_task('check gas', 1)

        self.assertEqual('get keys',pq.pop_task())
        self.assertEqual('turn on car', pq.pop_task())
        self.assertEqual('check gas', pq.pop_task())
        self.assertEqual('drive to work', pq.pop_task())
        self.assertEqual('park at work', pq.pop_task())

        with self.assertRaises(KeyError):
            pq.pop_task()