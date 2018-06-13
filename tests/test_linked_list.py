import unittest
from structures.linked_list import ListNode

class TestLinkedList(unittest.TestCase):

    def test_ll_contains_cycle(self):
        head = ListNode(3)
        head.next = ListNode(4)
        head.next.next = ListNode(5)
        cycle_start = ListNode(6)
        head.next.next.next = cycle_start
        cycle_start.next = ListNode(7)
        cycle_start.next.next = ListNode(8)
        cycle_start.next.next.next = cycle_start

        self.assertTrue(head.contains_cycle())

    def test_ll_no_cycle(self):
        head = ListNode(3)
        head.next = ListNode(4)
        head.next.next = ListNode(5)
        cycle_start = ListNode(6)
        head.next.next.next = cycle_start
        cycle_start.next = ListNode(7)
        cycle_start.next.next = ListNode(8)

        self.assertFalse(head.contains_cycle())
    
    def test_ll_cycle_on_single_node(self):
        self.assertFalse(ListNode(1).contains_cycle())

    def test_ll_get_cycle_start(self):
        head = ListNode(3)
        head.next = ListNode(4)
        head.next.next = ListNode(5)
        cycle_start = ListNode(6)
        head.next.next.next = cycle_start
        cycle_start.next = ListNode(7)
        cycle_start.next.next = ListNode(8)
        cycle_start.next.next.next = cycle_start

        self.assertEqual(cycle_start, head.get_beginning_of_cycle_if_exists())

    def test_ll_get_cycle_start_no_cycle(self):
        head = ListNode(3)
        head.next = ListNode(4)
        head.next.next = ListNode(5)
        cycle_start = ListNode(6)
        head.next.next.next = cycle_start
        cycle_start.next = ListNode(7)
        cycle_start.next.next = ListNode(8)

        self.assertEqual(None, head.get_beginning_of_cycle_if_exists())
    
    def test_ll_get_cycle_start_on_single_node(self):
        self.assertEqual(None, ListNode(1).get_beginning_of_cycle_if_exists())
    
    def test_reverse(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        self.assertEqual(1, head.val)
        self.assertEqual(2, head.next.val)
        self.assertEqual(3, head.next.next.val)
        head = head.reverse()
        self.assertEqual(3, head.val)
        self.assertEqual(2, head.next.val)
        self.assertEqual(1, head.next.next.val)
    
    def test_reverse_recursive(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        self.assertEqual(1, head.val)
        self.assertEqual(2, head.next.val)
        self.assertEqual(3, head.next.next.val)
        head = head.reverse_recursive()
        self.assertEqual(3, head.val)
        self.assertEqual(2, head.next.val)
        self.assertEqual(1, head.next.next.val)