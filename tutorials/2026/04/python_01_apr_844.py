# Merge Sort in Python
# =======================
# This is an implementation of the Merge Sort algorithm in Python.

def merge_sort(arr):
    # Base case: If the array has one or zero elements, it's already sorted.
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves of the array.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves into a single, sorted array.
    return merge(left_half, right_half)


def merge(left, right):
    # Create an empty list to store the merged result.
    merged = []
    
    # Compare elements from both lists and add the smaller one to the merged list.
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    
    # If there are remaining elements in either list, append them to the merged list.
    while len(left) > 0:
        merged.append(left.pop(0))
    while len(right) > 0:
        merged.append(right.pop(0))
    
    return merged


# Test the implementation
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)