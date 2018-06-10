def permutations_of_word(string: str):
    """
    Find all permutations of letters in a word.

    """
    def permute(current, remaining):
        if not remaining:
            permute.list.append(current)
            return
        for i in range(0,len(remaining)):
            remaining_minus = remaining[0:i] + remaining[i+1:]
            permute(current + remaining[i], remaining_minus)

    permute.list = []
    permute('', list(string))
    return permute.list
