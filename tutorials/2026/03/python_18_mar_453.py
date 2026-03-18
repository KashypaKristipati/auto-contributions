# Merge Sort Algorithm Implementation in Python

def merge_sort(arr):
    """
    Recursively splits the array into two halves until we have subarrays of size one.
    Then merges these subarrays back together in sorted order.
    """

    # Base case: if the length of the array is 1 or less, return it as it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point of the array
    mid = len(arr) // 2

    # Recursively call merge_sort on the left and right halves of the array
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the two sorted halves back together
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.
    """

    # Initialize an empty list to store our merged result
    merged = []

    # While we have elements in both the left and right arrays
    while len(left) > 0 and len(right) > 0:
        # Compare the smallest unmerged element from each array
        if left[0] <= right[0]:
            # If it's smaller, append it to our merged list
            merged.append(left.pop(0))
        else:
            # Otherwise, append the next element from the larger array
            merged.append(right.pop(0))

    # If there are any remaining elements in either the left or right arrays,
    # we'll append them all to the end of our merged list
    merged.extend(left)
    merged.extend(right)

    return merged


# Test the merge sort function with a random array
import random

random_array = [random.randint(0, 100) for _ in range(10)]
print("Unsorted array:", random_array)

sorted_array = merge_sort(random_array)
print("Sorted array:", sorted_array)