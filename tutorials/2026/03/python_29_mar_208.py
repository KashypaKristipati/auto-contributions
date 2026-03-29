# Two Pointers Technique in Python

def remove_duplicates(arr):
    """
    Removes duplicates from an array using the two pointers technique.

    Args:
        arr (list): The input array.

    Returns:
        list: The array with duplicates removed.
    """
    # Create a set to store unique elements
    unique_elements = set()
    
    # Initialize two pointers, one at the beginning and one at the end of the array
    left = 0
    right = 0
    
    # Traverse the array using the right pointer
    while right < len(arr):
        # If the element at the right pointer is not in the set of unique elements,
        # add it to the set and move both pointers forward
        if arr[right] not in unique_elements:
            unique_elements.add(arr[right])
            left += 1
            temp = arr[left]
            while left < len(arr) and arr[left] == temp:
                left += 1
            arr.pop(left - 1)
        right += 1
    
    return arr

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original array:", arr)

new_arr = remove_duplicates(arr)
print("Array with duplicates removed:", new_arr)