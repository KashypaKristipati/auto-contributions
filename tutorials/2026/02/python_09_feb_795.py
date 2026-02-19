# This script teaches the basics of using a hash map (dictionary) in Python.
# A hash map is a data structure that stores key-value pairs and allows for efficient lookups.

# Importing the built-in dictionary class
from collections import defaultdict, OrderedDict

# Creating an empty dictionary
hash_map = {}

# Adding some key-value pairs to our hash map
hash_map['apple'] = 5
hash_map['banana'] = 10
hash_map['cherry'] = 15

# Accessing a value by its key
print("Value of 'apple':", hash_map.get('apple'))

# Updating a value in the hash map
hash_map['apple'] = 20
print("Updated value of 'apple':", hash_map['apple'])

# Adding multiple values at once
hash_map.update({'banana': 15, 'date': 25})
print("Hash map after update:", hash_map)

# Checking if a key exists in the hash map
if 'cherry' in hash_map:
    print("'cherry' is in the hash map")
else:
    print("'cherry' is not in the hash map")

# Removing a key-value pair from the hash map
del hash_map['banana']
print("Hash map after removal:", hash_map)

# Creating an ordered dictionary
ordered_hash_map = OrderedDict()
ordered_hash_map['apple'] = 5
ordered_hash_map['banana'] = 10
ordered_hash_map['cherry'] = 15

# Printing the keys of the ordered dictionary in order
for key in ordered_hash_map:
    print(key)

# Creating a default dictionary
default_hash_map = defaultdict(int)
default_hash_map['apple'] = 5
default_hash_map['banana'] = 10

# Accessing a value from a default dictionary
print("Value of 'apple':", default_hash_map['apple'])

# Creating a hash map with specific keys and values
hash_map_dict = {'a': 1, 'b': 2, 'c': 3}
print(hash_map_dict)

# Example usage:
def test_hash_map():
    # Create an empty dictionary
    hash_map = {}

    # Add some key-value pairs to the hash map
    hash_map['name'] = 'John Doe'
    hash_map['age'] = 30

    # Access a value by its key
    print("Name:", hash_map.get('name'))

    # Update a value in the hash map
    hash_map['age'] += 5
    print("Updated age:", hash_map['age'])

test_hash_map()