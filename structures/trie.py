class Trie():

    eof = '__eof__'

    def __init__(self, words):
        self.head = {}
        for word in words:
            current = self.head
            for letter in word:
                current = current.setdefault(letter, {})
            current[self.eof] = self.eof
    
    def add(self, word):
        current = self.head
        for letter in word:
            current = current.setdefault(letter, {})
        current[self.eof] = self.eof
    
    def get_all_common_prefix(self, prefix):
        idx = 0
        node = self.head
        while idx < len(prefix):
            letter = prefix[idx]
            if letter not in node:
                return []
            node = node[letter]
            idx += 1
        # get all words after this node
        def getWords(node, prefix):
            if self.eof in node:
                return [prefix]
            words = []
            for key, val in node.items():
                words.extend(getWords(val, prefix + key))
            return words
        
        return getWords(node, prefix)
