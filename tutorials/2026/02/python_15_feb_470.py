# Binary Search Algorithm in Python

def binary_search(arr, target):
    # Initialize the low and high pointers to the start and end of the array
    low = 0
    high = len(arr) - 1
    
    # Continue searching while the low pointer is less than or equal to the high pointer
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        
        # If the target is found at the middle index, return its value
        if arr[mid] == target:
            return mid
        
        # If the target is less than the middle element, update the high pointer
        elif arr[mid] > target:
            high = mid - 1
        
        # If the target is greater than the middle element, update the low pointer
        else:
            low = mid + 1
    
    # If the target is not found in the array, return -1
    return -1

# Example usage
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
index = binary_search(arr, target)

if index != -1:
    print(f"Target {target} found at index {index}.")
else:
    print(f"Target {target} not found in the array.")