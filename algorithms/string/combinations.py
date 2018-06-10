def combinations_of_word(string: str):
    """
    Find all combinations of letters in a word.

    """
    output = []
    for i in range(0,len(string)):
        output.append(string[i])
        for j in range(i+1, len(string)):
            output.append(string[i:j+1])

    return output
