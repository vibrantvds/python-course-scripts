class AlgoHashTable:

    def __init__(self,size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self,key,value):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key,value))

    def get_val(self,key):
        pass

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_map = AlgoHashTable(256)
hash_map.set_val('mashrur@example.com','some value')
hash_map.set_val('johndoe@example.com','some other value')
print(hash_map)
hash_map.set_val('mashrur@example.com','I love Python')
print(hash_map)
