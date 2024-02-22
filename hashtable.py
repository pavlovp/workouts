class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.deleted = object()  # A unique marker for deleted entries

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        original_index = index
        while self.table[index] is not None and self.table[index] != self.deleted:
            if self.table[index][0] == key:
                # Update existing key
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
            if index == original_index:
                # The table is full
                raise Exception("Hash table is full")
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] != self.deleted and self.table[index][0] == key:
                # Key found
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                # Came back to the start, key not in table
                break
        return None  # Key not found

    def delete(self, key):
        index = self.hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] != self.deleted and self.table[index][0] == key:
                # Mark as deleted
                self.table[index] = self.deleted
                return True
            index = (index + 1) % self.size
            if index == original_index:
                # Came back to the start, key not in table
                break
        return False  # Key not found

# Example usage
hash_table = HashTable(10)  # Initialize a hash table with size 10
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
print(hash_table.search("key1"))  # Should print "value1"
print(hash_table.search("key3"))  # Should print None
hash_table.delete("key1")
print(hash_table.search("key1"))  # Should print None
