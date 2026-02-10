# Merge Sort Algorithm Implementation in Python

def merge_sort(arr):
    # If the array has 1 or fewer elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle of the array
    mid = len(arr) // 2

    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves back together
    return merge(left_half, right_half)


def merge(left, right):
    # Initialize an empty list to store the merged result
    merged = []

    # Loop through both lists simultaneously
    while len(left) > 0 and len(right) > 0:
        # Compare the current elements of both lists
        if left[0] <= right[0]:
            # Add the smaller element to the merged list
            merged.append(left.pop(0))
        else:
            # Add the larger element to the merged list
            merged.append(right.pop(0))

    # If there are remaining elements in either list, add them to the merged list
    merged.extend(left)
    merged.extend(right)

    return merged


# Test the merge sort algorithm
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original Array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted Array:", sorted_arr)