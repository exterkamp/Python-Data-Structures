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

def combinations_of_phone_input(string: str):
    """
    Find all permutations of phone numbers in an input of numbers.

    While not a 'combination' of numbers in the mathematical sense
    this is known more lexically as a combination.  But does not 
    contain all combinations possible.  Only combinations that are
    full length using all input numbers in the string.

    """
    phone_mapper = {
            '1' : [],
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z'],
        }
    
    outputs = [letter for letter in phone_mapper[string[0]]]
        
    for i in range(1,len(string)):
        temp = []
        for output in outputs:
            temp = temp + [output + letter for letter in phone_mapper[string[i]]]
        outputs = temp
    
    return outputs    




