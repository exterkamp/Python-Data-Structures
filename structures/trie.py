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