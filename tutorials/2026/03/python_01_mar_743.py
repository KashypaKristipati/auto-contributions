# Merge Sort Algorithm in Python

def merge_sort(arr):
    # Base case: If the array has 1 or fewer elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point of the array
    mid = len(arr) // 2

    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    # Initialize an empty list to store the merged result
    merged = []

    # While both lists have elements
    while len(left) > 0 and len(right) > 0:
        # Compare the smallest unmerged elements in both lists
        if left[0] <= right[0]:
            # Append the smaller element to the merged list
            merged.append(left.pop(0))
        else:
            # Append the smaller element to the merged list
            merged.append(right.pop(0))

    # If there are remaining elements in either list, append them to the merged list
    merged.extend(left)
    merged.extend(right)

    # Return the merged list
    return merged

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
print("Sorted array:", merge_sort(arr))