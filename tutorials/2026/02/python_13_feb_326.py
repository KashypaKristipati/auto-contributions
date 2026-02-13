# Binary Search Algorithm in Python

def binary_search(arr, target):
    # Initialize the low and high pointers
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Calculate the mid index
        mid = (low + high) // 2
        
        # Compare the target with the middle element
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # If the target is greater, move to the right half
            low = mid + 1
        else:
            # If the target is smaller, move to the left half
            high = mid - 1

    # Return -1 if the target is not found
    return -1


# Example usage
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the array")