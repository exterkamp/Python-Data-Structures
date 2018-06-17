def rabin_karp_find_substring(string, substring, base=256, prime_modulus=487):
    """
    Finds occurances of a substring in a string.

    This uses the Rabin-Karp rolling hash to calculate a rolling hash
    value for windows of letters in the string.  Since this is a rolling
    hash when going to a new number we can drop the number that will not
    be in the next window and add the new one to the hash.  Once the
    hashes are the same there is a candidate match and the strings must be
    examined letter by letter in case of hash collision.

    Args:
        string: the string that is being looked in
        substring: the string to search for
        base: the base used to calculate hashes
        prime_modulus: positive prime number used to bound the hash results 

    Returns:
        Index of the beginning of the first occurance
        of a substring that is within the string.

    """
    # substring hash
    substring_hash = 0
    rolling_hash = 0
    base_n = pow(base,len(substring)-1)%prime_modulus

    # get the initial hashes
    for i in range(len(substring)):
        rolling_hash = (base * rolling_hash + ord(string[i]))%prime_modulus
        substring_hash = (base * substring_hash + ord(substring[i]))%prime_modulus

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
        if i < len(string) - len(substring):
            # remove the ith number and add the i+len(substring)th number
            rolling_hash = ((rolling_hash - (base_n * ord(string[i]))) * base) + ord(string[i + len(substring)])%prime_modulus
            
            # make sure t >= 0
            rolling_hash = (rolling_hash + prime_modulus) % prime_modulus

    return -1
