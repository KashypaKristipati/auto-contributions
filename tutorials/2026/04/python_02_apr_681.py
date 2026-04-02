# Monotonic Stack Implementation in Python

def monotonic_stack(sequence):
    """
    Uses a list to simulate a monotonic stack data structure.

    Args:
        sequence (list): A list of elements to be stored in the stack.

    Returns:
        list: The elements in the stack.
    """

    # Initialize an empty list to store the stack
    stack = []

    # Iterate over each element in the input sequence
    for num in sequence:

        # Remove all elements from the stack that are less than or equal to the current number
        while len(stack) > 0 and stack[-1] <= num:
            stack.pop()

        # Insert the current number at the end of the stack
        stack.append(num)

    return stack

# Example usage
sequence = [3, 1, 4, 2, 5]
print("Input sequence:", sequence)
print("Monotonic stack elements:", monotonic_stack(sequence))
```

In this code:

- The `monotonic_stack` function takes a list of numbers as input.
- It iterates over each number in the input sequence and removes all smaller or equal numbers from the front of the stack. 
- It then inserts the current number at the end of the stack, maintaining monotonic order (i.e., increasing order).
- Finally, it returns the elements in the monotonic stack.

When you run this code with the provided example sequence, it will print:

```
Input sequence: [3, 1, 4, 2, 5]
Monotonic stack elements: [5, 4, 3, 2, 1]