# String Hashing in Python
# This script covers the basic concepts of string hashing using Python's built-in data structures and algorithms.

import hashlib

def string_hashing(s):
    """
    This function calculates the hash value of a given string.
    
    Parameters:
    s (str): The input string for which the hash value is to be calculated.
    
    Returns:
    int: The hash value of the input string.
    """

    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the bytes of the input string
    # Each character in the string is converted to its ASCII value and added to the hash
    hash_object.update(s.encode('utf-8'))

    # Get the hexadecimal representation of the hash value
    hex_dig = hash_object.hexdigest()

    # Convert the hexadecimal string to an integer
    hash_value = int(hex_dig, 16)

    return hash_value

def main():
    s1 = "Hello, World!"
    print("Input String: ", s1)
    
    # Calculate and display the hash value of the input string
    hash_value = string_hashing(s1)
    print("Hash Value: ", hash_value)


if __name__ == "__main__":
    main()