class HashMap():

    def __init__(self, buckets=256, hash_function=lambda key: hash(key)):
        self.buckets = [[] for i in range(buckets)]
        self.hash_function = hash_function
    
    def insert(self, key, value):
        hash_key = self.hash_function(key) % len(self.buckets)

        bucket = self.buckets[hash_key]

        for i, val in enumerate(bucket):
            # check if exists, and override
            if val[0] == key:
                bucket[i] = (key, value)
                return
        # insert new
        bucket.append((key, value))

    def get(self, key):
        hash_key = self.hash_function(key) % len(self.buckets)

        bucket = self.buckets[hash_key]

        for val in bucket:
            if val[0] == key:
                return val[1]
        # not found
        raise KeyError
    
    def delete(self, key):
        hash_key = hash(key) % len(self.buckets)

        bucket = self.buckets[hash_key]

        for i, val in enumerate(bucket):
            if val[0] == key:
                del bucket[i]
                return val
        raise KeyError

def djb2(key):
    """
    Classic hashing function by Bernstein.

    This algorithm (k=33) was first reported 
    by dan bernstein many years ago in comp.lang.c.
    """
    hash = 5381

    for letter in str(key):
        hash = ((hash << 5) + hash) + ord(letter)
    
    return hash

def sdbm(key):
    """
    This function is a good bit scrambling function.

    This algorithm was created for sdbm (a public-domain
     reimplementation of ndbm) database library.
    """
    hash = 0

    for letter in str(key):
        hash = ord(letter) + (hash << 6) + (hash << 16) - hash
    
    return hash

def lose_lose(key):
    """
    This hash function is extremely bad.  Don't use it.

    This hash function appeared in K&R (1st ed) but at least 
    the reader was warned: "This is not the best possible 
    algorithm, but it has the merit of extreme simplicity."
    """
    hash = 0

    for letter in str(key):
        hash += ord(letter)
    
    return hash