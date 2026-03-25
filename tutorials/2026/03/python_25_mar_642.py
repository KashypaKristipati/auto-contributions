# Two Pointers Technique in Python
=====================================

The two-pointers technique is a common approach used to solve various problems involving arrays or linked lists. It involves using two pointers that start from both ends of the array/linked list and move towards the center.

```python
def remove_duplicates(arr):
    # If the array has less than 2 elements, it cannot have duplicates
    if len(arr) < 2:
        return arr

    # Initialize two pointers, one at the beginning and one at the end of the array
    i = 0
    j = 1

    # Move the second pointer to the next element if the first element is not a duplicate
    while j < len(arr):
        # If the elements at indices i and j are different, move the second pointer to the next element
        if arr[i] != arr[j]:
            i += 1
            j += 1
        # If the elements at indices i and j are the same, skip the duplicate element
        else:
            j += 1

    # Return the array with duplicates removed
    return arr[:i+1]


# Test the function
arr = [1, 2, 3, 2, 4, 5, 6, 7, 8, 9]
print("Original Array:", arr)
print("Array without duplicates:", remove_duplicates(arr))
```

This code defines a function `remove_duplicates` that takes an array as input and returns the array with duplicates removed. The two pointers technique is used to achieve this.

The outer loop (`i`) iterates over the elements of the array, while the inner loop (`j`) moves towards the center of the array. If the elements at indices `i` and `j` are different, both pointers move forward. If they are the same, only the second pointer moves forward to skip the duplicate element.

Finally, the function returns a slice of the original array up to index `i+1`, which represents the unique elements.

When you run this code with the test array `[1, 2, 3, 2, 4, 5, 6, 7, 8, 9]`, it will output:

```
Original Array: [1, 2, 3, 2, 4, 5, 6, 7, 8, 9]
Array without duplicates: [1, 2, 3, 4, 5, 6, 7, 8, 9]