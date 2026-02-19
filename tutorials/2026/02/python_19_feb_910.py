# Dynamic Programming Memoization in Python
=====================================================

This script demonstrates the use of memoization to optimize a recursive function using dynamic programming.

```python
def fibonacci(n, memo={}):
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    
    # Check if result for n is already in memo
    if n not in memo:
        # If not, compute it and store in memo
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    
    # Return the computed result
    return memo[n]

# Example usage:
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")