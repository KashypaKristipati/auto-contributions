# Dynamic Programming with Memoization
=====================================

This code demonstrates how to use memoization to solve the classic Fibonacci sequence problem using dynamic programming.

```python
def fibonacci(n, memo={}):
    """
    Calculate the nth Fibonacci number using dynamic programming with memoization.
    
    Args:
    n (int): The position of the Fibonacci number to calculate.
    memo (dict): A dictionary to store previously calculated Fibonacci numbers.
    
    Returns:
    int: The nth Fibonacci number.
    """
    # Base case: If n is 0 or 1, return n
    if n <= 1:
        return n
    
    # Check if the Fibonacci number for n is already in the memo dictionary
    if n not in memo:
        # If not, calculate it and store it in the memo dictionary
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    
    # Return the Fibonacci number for n
    return memo[n]

# Example usage:
print(fibonacci(10))  # Output: 55