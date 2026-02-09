# Binary Search in Python
=====================================

## Overview
Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

## Code

```python
def binary_search(arr, target):
    """
    Searches for an element in a sorted array using binary search.
    
    Args:
        arr (list): A sorted list of elements.
        target: The element to be searched in the list.
        
    Returns:
        int: The index of the target element if found, -1 otherwise.
    """
    low = 0
    high = len(arr) - 1
    
    # Continue searching while the two pointers haven't crossed each other
    while low <= high:
        mid = (low + high) // 2
        
        # If the middle element is the target, return its index
        if arr[mid] == target:
            return mid
        # If the middle element is less than the target, move the left pointer to the right half
        elif arr[mid] < target:
            low = mid + 1
        # If the middle element is greater than the target, move the right pointer to the left half
        else:
            high = mid - 1
    
    # If the loop ends without finding the target, it's not in the array
    return -1

# Example usage
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")