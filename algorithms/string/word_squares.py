import structures
from structures.trie import Trie

def word_squares(words):

    trie = Trie(words)

    def construct(square):
        if len(square) == len(square[0]):
            construct.squares.append(square)
            return
        # find prefix, based on len of square
        prefix = ""
        idx = len(square)
        for i in range(idx):
            prefix += square[i][idx]
        # get all prefix words
        prefix_words = trie.get_all_common_prefix(prefix)
        for prefix_word in prefix_words:
            construct(square + [prefix_word])
        
    construct.squares = []

    # start all squares
    for word in words:
        construct([word])

    return construct.squares
