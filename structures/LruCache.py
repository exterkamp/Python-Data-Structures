class ListNode:

    """

    Doubly Linked List node.

    This is a list node that can link to a previous value,
    and a next value.  The node contains a key and a value pair.


    """

    def __init__(self, key, val):
        """
        Create a node.

        Node will have a key and value, and blank
        previous and next values.

        :param key: the lookup key value
        :param val: the value corresponding to the key
        """
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LruCache:

    """

    Least Recently Used Cache (LRU Cache)

    Data structure to store and lookup values by keys.  Keys can be any type and values
    can be any type.  The cache has a set capacity and will drop off values when the
    capacity is reached.  The cache will drop the value that was used the farthest
    back in time (least recently used).

    The cache uses a dictionary for fast lookups of values, and a linked list to keep
    track of the least recently used key:value for dropping.

    Time complexity:
        put: O(1), amortized worst case: O(N)
        get: O(1), amortized worst case: O(N)

    """

    terminal_value = 0
    """
    Constant value used by the head and tail as terminating values.
    """

    def __init__(self, capacity):
        """
        Create an LRU Cache.

        :param capacity: the maximum number of elements that can be stored in the cache,
            must be greater than 0
        """
        if capacity <= 1:
            raise ValueError("Capacity must be >= 1")

        # init the head and tail nodes
        self.head = ListNode(self.terminal_value, self.terminal_value)
        self.tail = ListNode(self.terminal_value, self.terminal_value)

        # initialize the head and tail to point to each other
        self.head.next = self.tail
        self.tail.prev = self.head

        # initialize the lookup map
        self.lookup_map = {}

        # the max number of elements allowed in the cache
        self.capacity = capacity

    def put(self, key, value):
        """
        Add a value to the cache.

        If adding the value will cause the cache to go above capacity, then
        the least recently item will be dropped.

        :param key: the lookup key of the item
        :param value: the value stored on key
        :return: None
        """
        # check if the key is in the lookup map
        if key in self.lookup_map:
            # remove the node from map and the list
            node = self.lookup_map.pop(key)
            self._remove(node)

        # make a new node with the value
        node = ListNode(key, value)

        # add the node to the list
        self._add(node)

        # add the node to the lookup map
        self.lookup_map[key] = node

        # check the capacity
        if len(self.lookup_map) > self.capacity:
            # remove the last node
            least_recently_used_node = self.head.next

            # remove from the linked list
            self._remove(least_recently_used_node)

            # remove from the lookup map
            del self.lookup_map[least_recently_used_node.key]

    def get(self, key):
        """
        Get a value from the cache.

        This will reset the key in the drop order.

        :param key: the key to lookup
        :return: the value of the key or -1 if the key is not found
        """
        # check if the key is in the lookup
        if key in self.lookup_map:
            # get the node
            node = self.lookup_map[key]

            # remove the node from the linked list
            self._remove(node)

            # add the node to the end of the linked list
            self._add(node)

            return node.val
        else:
            return -1

    def _add(self, node):
        """
        Internal function.  Add a node to the end of the LRU list.

        This function will add a node immediately in front of the tail
        node.  Sets the node previous to the tail to the previous of
        the new node, and the next of the new node to the tail.

        :param node:m the node to add to the list
        :return: None
        """
        old_last_node = self.tail.prev

        # set node's previos to old prev
        node.prev = old_last_node

        # set node's next to tail
        node.next = self.tail

        # set old last node next to node
        old_last_node.next = node

        # set tail's prev to node
        self.tail.prev = node

    def _remove(self, node):
        """
        Internal function.  Remove a node from the list.

        This function will remove a node by getting its prev and next
        and linking them together, thus removing the node and allowing
        it to be garbage collected.

        :param node: the node to remove from the list
        :return: None
        """

        # get the previous and next from the node
        previous_node = node.prev
        next_node = node.next

        # set the prev next to the next
        previous_node.next = next_node

        # set the next prev to the prev
        next_node.prev = previous_node
