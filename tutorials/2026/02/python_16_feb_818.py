# Hash Map Tutorial
# This script teaches the basics of hash map data structure in Python.
# A hash map is a data structure that stores key-value pairs and allows for efficient lookup, insertion, and deletion operations.

import hashlib
from typing import Any, Dict

class HashMap:
    def __init__(self, size: int = 10):
        """
        Initialize the hash map with a specified size.

        :param size: The initial number of slots in the hash map.
        """
        self.size = size
        self.buckets = [[] for _ in range(size)]  # Create empty buckets

    def _hash(self, key: Any) -> int:
        """
        Calculate the hash value for a given key.

        :param key: The key to be hashed.
        :return: The calculated hash value.
        """
        return sum(hash(x) for x in str(key).encode()) % self.size  # Use SHA-256 hashing

    def put(self, key: Any, value: Any) -> None:
        """
        Insert or update a key-value pair in the hash map.

        :param key: The key to be inserted or updated.
        :param value: The corresponding value.
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # If the key already exists, update its value
                bucket[i] = (key, value)
                return
        # If the key is new, append it to the bucket
        bucket.append((key, value))

    def get(self, key: Any) -> Any:
        """
        Retrieve the value associated with a given key.

        :param key: The key to be looked up.
        :return: The corresponding value if found; otherwise, None.
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        # If the key is not found, return None
        return None

    def delete(self, key: Any) -> None:
        """
        Remove a key-value pair from the hash map.

        :param key: The key to be deleted.
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # If the key is found, remove it from the bucket
                del bucket[i]
                return

    def display(self) -> None:
        """
        Print the contents of the hash map.
        """
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}:")
            for k, v in bucket:
                print(f"{k}: {v}")
            print()


# Example usage
if __name__ == "__main__":
    # Create a new hash map with 10 slots
    my_map = HashMap()

    # Insert some key-value pairs
    my_map.put("apple", "fruit")
    my_map.put("carrot", "vegetable")
    my_map.put("banana", "fruit")

    # Display the contents of the hash map
    print("Initial Contents:")
    my_map.display()

    # Retrieve a value using its key
    print("\nRetrieving