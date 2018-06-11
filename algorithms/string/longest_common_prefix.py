from functools import reduce
from structures.trie import Trie

def find_longest_common_prefix(words:list):
    """
    Find the longest common prefix in a list of words.

    """
    trie = Trie(words)

    head = trie.head

    prefix = []

    while len(head) == 1 and trie.eof not in head:
        key, value = head.popitem()
        prefix.append(key)
        head = value
    
    return "".join(prefix)

def find_longest_common_prefix_reduce(words:list):
    """
    Find the lcp in a list of words, using 'reduce' functions.

    """
    if not words:
        return ''
    
    def common_start(w1, w2):
        shorter = w1 if len(w1) < len(w2) else w2
        for i in range(0, len(shorter)):
            if w1[i] != w2[i]:
                return shorter[:i]
        return shorter
    
    return reduce(common_start, words)
