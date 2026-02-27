# Dynamic Programming with Memoization

def fibonacci(n, memo={}):
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Check if result is already in memo
    elif n in memo:
        return memo[n]
    # If not, calculate result and store in memo
    else:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        memo[n] = result
        return result

def fibonacci_dp(n):
    # Create a list to store the Fibonacci sequence
    fib_sequence = [0] * (n + 1)
    # Base cases
    fib_sequence[0] = 0
    fib_sequence[1] = 1
    # Fill in the rest of the sequence
    for i in range(2, n + 1):
        fib_sequence[i] = fib_sequence[i-1] + fib_sequence[i-2]
    # Return the nth Fibonacci number
    return fib_sequence[n]

# Example usage
print("Fibonacci using memoization:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

print("\nFibonacci using dynamic programming:")
for i in range(10):
    print(f"F({i}) = {fibonacci_dp(i)}")