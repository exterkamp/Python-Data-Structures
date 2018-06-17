def rabin_karp_find_substring(string, substring, base=256):
    """
    Finds occurances of a substring in a string.

    Args:
        string: the string that is being looked in
        substring: the string to search for

    Returns:
        Index of the beginning of the first occurance
        of a substring that is within the string.

    """
    # substring hash
    substring_hash = 0
    rolling_hash = 0

    # get the initial hashes
    for i in range(len(substring)):
        rolling_hash = rolling_hash_ord(rolling_hash, base, len(substring) - i - 1, additional_element=string[i])
        substring_hash = rolling_hash_ord(substring_hash, base, len(substring) - i - 1, additional_element=substring[i])
    
    for i in range(len(string) - len(substring)+1):
        # check if hash matches hash of substring
        if rolling_hash == substring_hash:
            # check if the letters are 1:1
            for s_i, letter in enumerate(substring):
                if letter != string[i+s_i]:
                    break
            else:
                return i
        # recalulate hash
        if i+len(substring) <= len(string) - 1:
            rolling_hash = rolling_hash_ord(rolling_hash, base, len(substring)-1, removal_element=string[i], additional_element=string[i+len(substring)])
    return -1

def rolling_hash_ord(previous_hash, base, length, removal_element=None, additional_element=None):
    if removal_element and additional_element:
        previous_hash -= ord(removal_element) * (base ** length)
        previous_hash *= base
        previous_hash += ord(additional_element)
    elif additional_element:
        previous_hash += ord(additional_element) * (base ** length)
    return previous_hash
