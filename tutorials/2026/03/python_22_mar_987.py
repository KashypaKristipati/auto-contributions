# Sliding Window Technique in Python
=====================================

The sliding window technique is a common approach used to solve problems that involve finding substrings or ranges within a larger sequence.

```python
def max_sum_subarray(arr, k):
    """
    Find the maximum sum of a subarray of size k.
    
    Parameters:
    arr (list): The input array.
    k (int): The size of the sliding window.
    
    Returns:
    int: The maximum sum of a subarray of size k.
    """
    # Initialize the maximum sum and the current sum
    max_sum = float('-inf')
    current_sum = 0
    
    # Calculate the sum of the first window
    for i in range(k):
        current_sum += arr[i]
    
    # Update the maximum sum
    max_sum = max(max_sum, current_sum)
    
    # Slide the window to the right
    for i in range(k, len(arr)):
        # Subtract the leftmost element and add the new element
        current_sum = current_sum - arr[i-k] + arr[i]
        
        # Update the maximum sum
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def max_product_subarray(arr):
    """
    Find the maximum product of a subarray.
    
    Parameters:
    arr (list): The input array.
    
    Returns:
    int: The maximum product of a subarray.
    """
    # Initialize the maximum and minimum product ending at the current position
    max_product = float('-inf')
    min_product = float('inf')
    
    # Calculate the product of the first window
    for num in arr:
        if num < 0:
            max_product, min_product = min_product, max_product
        
        # Update the maximum and minimum product
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)
    
    return max_product

# Test the functions
arr1 = [1, 2, -3, 4]
k1 = 3
print(max_sum_subarray(arr1, k1))  # Output: 6

arr2 = [-2, 1, -3, 5, -6]
print(max_product_subarray(arr2))  # Output: 10