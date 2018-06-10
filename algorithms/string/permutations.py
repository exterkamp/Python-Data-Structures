def permutations_of_word(string: str):
    """
    Find all permutations of letters in a word.

    """
    def permute(current, remaining):
        if not remaining:
            permute.list.append(current)
            return
        for i in range(0,len(remaining)):
            permute(current + remaining[i], remaining[:i] + remaining[i+1:])

    permute.list = []
    permute('', list(string))
    return permute.list
