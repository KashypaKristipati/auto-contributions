# Hash Map Usage in Python
=====================================

This script teaches the basics of using a hash map (also known as a dictionary) in Python.
A hash map is a data structure that stores key-value pairs and allows for efficient lookup, insertion, and deletion.

```python
import hashlib

class HashMap:
    def __init__(self, size=10):
        # Initialize an empty array to store the hash map
        self.size = size
        self.map = [[] for _ in range(size)]

    def _hash(self, key):
        # Calculate the hash value using SHA-256
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.size

    def insert(self, key, value):
        # Get the index of the bucket where the key-value pair should be stored
        index = self._hash(key)
        
        # Check if the key already exists in the map
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                self.map[index][i] = (key, value)
                return
        
        # If not, add the key-value pair to the bucket
        self.map[index].append((key, value))

    def get(self, key):
        # Get the index of the bucket where the key should be found
        index = self._hash(key)
        
        # Iterate through each key-value pair in the bucket
        for k, v in self.map[index]:
            if k == key:
                return v
        
        # If not found, return None
        return None

    def delete(self, key):
        # Get the index of the bucket where the key should be deleted
        index = self._hash(key)
        
        # Iterate through each key-value pair in the bucket
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                del self.map[index][i]
                return

# Test the hash map
if __name__ == "__main__":
    hash_map = HashMap()
    
    # Insert some key-value pairs
    hash_map.insert("apple", 5)
    hash_map.insert("banana", 7)
    hash_map.insert("orange", 3)
    
    # Get a value from the map
    print(hash_map.get("apple"))  # Output: 5
    
    # Delete a key-value pair
    hash_map.delete("banana")
    
    # Try to get a deleted value
    print(hash_map.get("banana"))  # Output: None