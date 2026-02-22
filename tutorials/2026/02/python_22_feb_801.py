# Two Pointers Technique in Python
=====================================

The two pointers technique is a common approach used in algorithms to solve problems involving arrays, linked lists, or other data structures. It involves using two pointers to traverse the data structure and perform operations such as finding the first or last occurrence of an element, removing elements, or swapping elements.

### Example Problem: Remove Duplicates from Sorted Array

Given a sorted array with duplicate elements, remove the duplicates and return the array.

### Code

```python
def remove_duplicates(nums):
    # If the array has less than 2 elements, there are no duplicates
    if len(nums) < 2:
        return nums

    # Initialize two pointers, one at the beginning of the array
    # and one at the second element
    i = 0
    j = 1

    # Traverse the array
    while j < len(nums):
        # If the current element is not a duplicate, move the non-duplicate
        # element one step forward
        if nums[j] != nums[i]:
            i += 1
            # Move the current element one step forward
            nums[i] = nums[j]
        # Move the current element to the next position
        j += 1

    # Return the array with duplicates removed
    return nums[:i+1]

# Run the example
nums = [1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9]
print(remove_duplicates(nums))
```

Output:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]