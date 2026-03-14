# String Hashing in Python
#=====================================

def calculate_hash(s):
    # Calculate the hash value using the built-in hash() function
    hash_value = hash(s)
    return hash_value

def djb2_hash(s):
    # Initialize the hash value to 5381
    hash_value = 5381
    
    # Iterate over each character in the string
    for char in s:
        # Multiply the current hash value by 33 and add the ASCII value of the character
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
    
    return hash_value

def fnv_1a_hash(s):
    # Initialize the hash value to the FNV offset basis (2166136261)
    hash_value = 2166136261
    
    # Calculate the prime number for the FNV hash function
    fnv_prime = 16777219
    
    # Iterate over each character in the string
    for char in s:
        # Multiply the current hash value by the FNV prime and add the ASCII value of the character
        hash_value = (hash_value ^ ord(char)) * fnv_prime
    
    return hash_value

def string_hashing_example():
    # Test strings
    test_strings = ['Hello, World!', 'Python is awesome', 'Hashing in Python']
    
    # Hash each string using the djb2 algorithm
    print('DJB2 Hashes:')
    for s in test_strings:
        print(f'{s}: {djb2_hash(s)}')
    
    # Hash each string using the FNV 1a algorithm
    print('\nFNV 1a Hashes:')
    for s in test_strings:
        print(f'{s}: {fnv_1a_hash(s)}')

string_hashing_example()