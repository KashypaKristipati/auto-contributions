def binary_search(arr, target):
    # Initialize two pointers, one at the start and one at the end of the array
    left = 0
    right = len(arr) - 1

    # Continue the search until the two pointers meet
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2

        # Compare the middle element to the target
        if arr[mid] == target:
            # If they match, return the middle index
            return mid
        elif arr[mid] < target:
            # If the middle element is less than the target, move the left pointer to the right
            left = mid + 1
        else:
            # If the middle element is greater than the target, move the right pointer to the left
            right = mid - 1

    # If the target is not found, return -1
    return -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
index = binary_search(arr, target)

if index != -1:
    print("Target found at index", index)
else:
    print("Target not found in the array")

# Test case with a sorted array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9
index = binary_search(arr, target)

if index != -1:
    print("Target found at index", index)
else:
    print("Target not found in the array")

# Test case with an unsorted array
import random
arr = [random.randint(1, 100) for _ in range(10)]
target = random.randint(1, 100)
index = binary_search(arr, target)

if index != -1:
    print("Target found at index", index)
else:
    print("Target not found in the array")