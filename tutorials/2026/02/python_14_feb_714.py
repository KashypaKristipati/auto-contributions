# Bit Manipulation Tricks in Python

# This script teaches bit manipulation tricks and their applications.
# Bit manipulation is a technique used to manipulate bits (binary digits) in computer programming.

def get_bit(n, pos):
    """
    Returns the bit at the given position in the binary representation of n.
    
    Parameters:
    n (int): The number to extract a bit from.
    pos (int): The position of the bit to extract (0-indexed).
    
    Returns:
    int: The bit at the given position.
    """
    # Create a mask with all bits set to 1 except for the bit at the given position
    mask = ~(1 << pos)
    # Use bitwise AND operation to get the bit at the given position
    return (n & mask) >> pos

def set_bit(n, pos):
    """
    Sets the bit at the given position in the binary representation of n.
    
    Parameters:
    n (int): The number to set a bit on.
    pos (int): The position of the bit to set (0-indexed).
    
    Returns:
    int: The number with the bit at the given position set.
    """
    # Create a mask with all bits set to 1 except for the bit at the given position
    mask = ~(1 << pos)
    # Use bitwise OR operation to set the bit at the given position
    return n | (mask << pos)

def clear_bit(n, pos):
    """
    Clears the bit at the given position in the binary representation of n.
    
    Parameters:
    n (int): The number to clear a bit from.
    pos (int): The position of the bit to clear (0-indexed).
    
    Returns:
    int: The number with the bit at the given position cleared.
    """
    # Create a mask with all bits set to 1 except for the bit at the given position
    mask = ~(1 << pos)
    # Use bitwise AND operation to clear the bit at the given position
    return n & ~mask

def toggle_bit(n, pos):
    """
    Toggles the bit at the given position in the binary representation of n.
    
    Parameters:
    n (int): The number to toggle a bit on.
    pos (int): The position of the bit to toggle (0-indexed).
    
    Returns:
    int: The number with the bit at the given position toggled.
    """
    # Use bitwise XOR operation to toggle the bit at the given position
    return n ^ (1 << pos)

def count_set_bits(n):
    """
    Counts the number of set bits in the binary representation of n.
    
    Parameters:
    n (int): The number to count set bits from.
    
    Returns:
    int: The number of set bits in the binary representation of n.
    """
    # Initialize a variable to store the count
    count = 0
    # Loop until all bits have been checked
    while n:
        # Increment the count if the least significant bit is set
        count += n & 1
        # Right shift to move to the next bit
        n >>= 1
    return count

def main():
    # Test the functions
    print("Testing get_bit function:")
    print(get_bit(10, 0))  # Output: 0
    print