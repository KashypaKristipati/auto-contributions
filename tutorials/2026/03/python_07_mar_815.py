# Prefix Sum Algorithm in Python
=====================================

## Overview

The prefix sum algorithm is a dynamic programming technique used to solve a variety of problems that require cumulative sums. This code implementation demonstrates how to use the prefix sum algorithm to solve a common problem: calculating the sum of elements in a list from a given index to the end.

## Code

```python
def prefix_sum(arr):
    """
    Calculate the prefix sum of an array.

    Args:
        arr (list): The input array.

    Returns:
        list: The prefix sum array.
    """
    # Initialize the prefix sum array with the first element of the input array
    prefix_sum_arr = [arr[0]]

    # Iterate over the input array starting from the second element
    for i in range(1, len(arr)):
        # Calculate the prefix sum at the current index by adding the current element to the previous prefix sum
        prefix_sum_arr.append(prefix_sum_arr[i-1] + arr[i])

    return prefix_sum_arr

def prefix_sum_query(prefix_sum_arr, start, end):
    """
    Query the prefix sum array for the sum of elements from the start index to the end index.

    Args:
        prefix_sum_arr (list): The prefix sum array.
        start (int): The start index.
        end (int): The end index.

    Returns:
        int: The sum of elements from the start index to the end index.
    """
    # Check if the start index is less than or equal to the end index
    if start > end:
        return 0
    # Return the difference between the prefix sum at the end index and the prefix sum at the start index minus one
    return prefix_sum_arr[end] - prefix_sum_arr[start-1]

# Example usage
arr = [1, 2, 3, 4, 5]
prefix_sum_arr = prefix_sum(arr)
print(prefix_sum_arr)  # Output: [1, 3, 6, 10, 15]

start = 2
end = 4
result = prefix_sum_query(prefix_sum_arr, start, end)
print(result)  # Output: 9