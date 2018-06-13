class ListNode():

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def contains_cycle(self):
        # the list is only 1 node long, which cannot contain a cycle
        if not self.next:
            return False
        slow_pointer = self.next        
        fast_pointer = self.next.next

        while slow_pointer is not fast_pointer:
            if slow_pointer:
                slow_pointer = slow_pointer.next
            if fast_pointer and fast_pointer.next:
                fast_pointer = fast_pointer.next.next
        if slow_pointer is None:
            return False
        else:
            return True
    
    def get_beginning_of_cycle_if_exists(self):
        # the list is only 1 node long, which cannot contain a cycle
        if not self.next:
            return None
        slow_pointer = self.next
        fast_pointer = self.next.next

        while slow_pointer is not fast_pointer:
            if slow_pointer:
                slow_pointer = slow_pointer.next
            if fast_pointer and fast_pointer.next:
                fast_pointer = fast_pointer.next.next
        if slow_pointer is None:
            return None
        # reset slow pointer
        slow_pointer = self
        # move the pointers again at same speed, will meet at start
        while slow_pointer is not fast_pointer:
            # print(slow_pointer.val, fast_pointer.val)
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        
        return slow_pointer

    def reverse(self):
        prev = None
        head = self
        while head.next:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        head.next = prev
        return head

    def reverse_recursive(self):
        def rev(node):
            if not node.next:
                rev.head = node
                return
            rev(node.next)
            temp = node.next
            temp.next = node
            node.next = None
        rev.head = self
        rev(self)

        return rev.head
