# Divide and Conquer Tutorial in Python

def merge_sort(arr):
    # If the array has one or zero elements, it is already sorted.
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    print("Splitting array:", arr)
    print("Left half:", left_half)
    print("Right half:", right_half)
    
    # Recursively sort both halves of the array.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    print("Recursively sorting arrays:")
    print("Left half:", left_half)
    print("Right half:", right_half)
    
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    # Compare elements from both halves and add the smaller one to the result.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Add any remaining elements from the left or right halves.
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    print("Merging array:", left, "and", right)
    print("Result:", merged)
    
    return merged


# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)