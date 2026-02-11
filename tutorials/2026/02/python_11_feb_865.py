# Sliding Window Technique in Python
=====================================================

This code demonstrates the use of the sliding window technique in Python to solve a common problem in algorithms.

```python
def max_sum_subarray(arr, k):
    """
    This function returns the maximum sum of a subarray of size k.
    
    Parameters:
    arr (list): The input array.
    k (int): The size of the subarray.
    
    Returns:
    int: The maximum sum of a subarray of size k.
    """
    # Initialize the maximum sum and the current sum
    max_sum = float('-inf')
    current_sum = 0
    
    # Calculate the sum of the first window
    for i in range(k):
        current_sum += arr[i]
    
    # Update the maximum sum if the first window has a larger sum
    max_sum = max(max_sum, current_sum)
    
    # Slide the window to the right
    for i in range(k, len(arr)):
        # Subtract the element that is leaving the window and add the new element
        current_sum = current_sum - arr[i-k] + arr[i]
        
        # Update the maximum sum if the current window has a larger sum
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 3
print("Maximum sum of subarray of size", k, "is:", max_sum_subarray(arr, k))
```

When you run this code with the example array and window size `3`, it will print:

```
Maximum sum of subarray of size 3 is: 12