class HashMap():

    def __init__(self):
        self.buckets = [[] for i in range(256)]
    
    def insert(self, key, value):
        hash_key = hash(key) % len(self.buckets)

        bucket = self.buckets[hash_key]

        for i, val in enumerate(bucket):
            # check if exists, and override
            if val[0] == key:
                bucket[i] = (key, value)
                return
        # insert new
        bucket.append((key, value))

    def get(self, key):
        hash_key = hash(key) % len(self.buckets)

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