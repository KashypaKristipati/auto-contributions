# Merge Sort Algorithm in Python

# Merge Sort is a divide-and-conquer algorithm that splits an array into two halves,
# recursively sorts them, and then merges them back together in sorted order.

def merge_sort(arr):
    # Base case: If the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point of the array
    mid = len(arr) // 2

    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the two sorted halves back together
    return merge(left_half, right_half)


def merge(left, right):
    # Initialize an empty list to store the merged result
    merged = []

    # Compare elements from the two lists and add the smaller one to the merged list
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    # If there are remaining elements in either list, append them to the merged list
    merged.extend(left)
    merged.extend(right)

    # Return the merged list
    return merged


# Test the merge sort algorithm
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)