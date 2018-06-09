class HashMap():
    """
    Data structure that stores key:value pairs.
    """

    def __init__(self, buckets=256, hash_function=lambda key: hash(key)):
        self.buckets = [[] for i in range(buckets)]
        self.hash_function = hash_function
    
    def insert(self, key, value):
        """
        Insert a key into the hash map.

        Insert a key into the map.  Internally the
        key is hashed with the internal hashing_function
        and placed into a bucket.  If the bucket  contains
        an element with the same key that keys value 
        will be overridden.

        Args:
            key: the key that will be hashed to index 
                the value 
            value: the value that will be stored at
                the index of 'key'

        Returns:
            None 
        """
        # hash the key and map that hash to a bucket
        hash_key = self.hash_function(key) % len(self.buckets)

        bucket = self.buckets[hash_key]

        for i, val in enumerate(bucket):
            # check if exists, and override if so
            if val[0] == key:
                bucket[i] = (key, value)
                return
        # insert new
        bucket.append((key, value))

    def get(self, key):
        """
        Get a value from the map.

        Args:
            key: the identifying key which will have its
                value returned
        
        Returns:
            The value that is stored within key.

        Raises:
            KeyError: Raised when key cannot be found.
        """
        # hash the key and map that hash to a bucket
        hash_key = self.hash_function(key) % len(self.buckets)

        bucket = self.buckets[hash_key]

        # find that key in the bucket
        for val in bucket:
            if val[0] == key:
                return val[1]
        
        raise KeyError
    
    def delete(self, key):
        """
        Delete a key from the map.

        Args:
            key: the key to delete
        
        Returns:
            The value of the key that was deleted.

        Raises:
            KeyError: Raised when the key cannot be found.
        """
        # hash the key and map that hash to a bucket
        hash_key = self.hash_function(key) % len(self.buckets)

        bucket = self.buckets[hash_key]

        # find the key in the bucket, delete it, and return it
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