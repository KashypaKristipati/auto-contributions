# Two Pointer Approach in Python

This script teaches you how to use the two pointer approach to solve problems efficiently. The two pointer technique is a common algorithm used for solving various problems like finding pairs with given sum, checking if an array can be sorted in O(n log n) time, and more.

## How it Works:

- We have two pointers, one at the beginning of the array and another at the end.
- We move these pointers towards each other based on certain conditions. If the elements at both ends are equal, we remove them from the array and continue with the next pair of elements.
- The key idea is to use the fact that as we move the pointers closer together, the difference between the elements at the two pointers decreases.

```python
def two_pointer_approach(array):
    # Initialize two pointers, one at the start and one at the end of the array
    left = 0
    right = len(array) - 1
    
    # Continue the process until the two pointers meet
    while left < right:
        # Calculate the sum of elements at current positions of both pointers
        current_sum = array[left] + array[right]
        
        # If the sum is equal to zero, remove this pair from the array and move both pointers
        if current_sum == 0:
            array.pop(left)
            array.pop(right - 1)  # Subtract 1 because we've already removed an element
            left += 1
            right -= 1
        # If the sum is less than zero, move the left pointer to increase the sum
        elif current_sum < 0:
            left += 1
        # If the sum is greater than zero, move the right pointer to decrease the sum
        else:
            right -= 1
    
    return array

# Example usage:
array = [2, -2, 4, -3, 5]
print("Original Array:", array)
new_array = two_pointer_approach(array)
print("Array after applying Two Pointer Approach:", new_array)