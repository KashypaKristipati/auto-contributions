# Divide and Conquer
#=====================

## Introduction

Divide and Conquer is a popular algorithmic technique used to solve complex problems by breaking them down into smaller sub-problems. This approach has been widely used in various fields such as computer science, mathematics, and engineering.

## Merge Sort Algorithm

This example demonstrates the implementation of Merge Sort, a classic Divide and Conquer algorithm.

```python
# Merge Sort function
def merge_sort(arr):
    # Base case: If the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle index to divide the array into two halves
    mid = len(arr) // 2

    # Recursively sort the left and right halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted left and right halves
    return merge(left_half, right_half)

# Merge function
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Compare elements from both halves and merge them
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left or right halves
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

# Test the Merge Sort function
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
print("Sorted array:", merge_sort(arr))