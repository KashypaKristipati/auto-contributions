# Sliding Window Technique in Python

def max_sum_subarray(arr, k):
    """
    Returns the maximum sum of a subarray of size k.
    
    :param arr: The input array.
    :param k: The size of the subarray.
    :return: The maximum sum of a subarray of size k.
    """
    # Initialize the window sum and the maximum sum found so far
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window through the array
    for i in range(k, len(arr)):
        # Subtract the element going out of the window and add the element coming in
        window_sum = window_sum - arr[i - k] + arr[i]
        # Update the maximum sum if the current window sum is greater
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 3
print("Maximum sum of subarray of size", k, "is:", max_sum_subarray(arr, k))

# Run the example
arr = [1, 2, 3, 4, 5]
k = 3
print("Maximum sum of subarray of size", k, "is:", max_sum_subarray(arr, k))