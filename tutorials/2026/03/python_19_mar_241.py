# Divide and Conquer in Python

def merge_sort(arr):
    # Base case: If the array has one or zero elements, it's already sorted.
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    # Recursively divide the array into two halves.
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the two sorted halves back together.
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    # Compare elements from both arrays and add the smaller one to the merged array.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Add any remaining elements from both arrays.
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    return merged


# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)