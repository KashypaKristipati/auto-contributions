# Monotonic Stack Implementation in Python
=====================================================

This implementation teaches how to use a monotonic stack to solve problems that require keeping track of the smallest or largest element seen so far.

A monotonic stack is a type of stack where all elements are either monotonically increasing or decreasing. This property allows us to keep track of the minimum or maximum value seen so far in O(1) time complexity.

## Implementation
---------------

```python
class MonotonicStack:
    def __init__(self):
        # Initialize an empty list to store the stack elements
        self.stack = []
        
        # Initialize a dictionary to store the indices of each element
        self.indices = {}

    def push(self, x):
        # While the stack is not empty and the top element is greater than the new element
        while len(self.stack) > 0 and self.stack[-1] > x:
            # Pop the last element from the stack
            old_index = self.indices.pop(self.stack.pop())
            # Update the indices of the elements that were popped
            for i in range(old_index, len(self.stack)):
                self.indices[self.stack[i]] = i - 1
        
        # Push the new element onto the stack
        self.stack.append(x)
        # Store the index of the new element
        self.indices[x] = len(self.stack) - 1

    def pop(self):
        # Check if the stack is empty
        if not self.stack:
            return None
        # Pop the top element from the stack
        x = self.stack.pop()
        # Remove the index of the popped element from the indices dictionary
        del self.indices[x]
        # Update the indices of the remaining elements in the stack
        for i in range(len(self.stack)):
            self.indices[self.stack[i]] = i
        return x

    def top(self):
        # Check if the stack is empty
        if not self.stack:
            raise ValueError("Stack is empty")
        # Return the top element of the stack
        return self.stack[-1]

    def contains(self, x):
        # Check if the index of the element exists in the indices dictionary
        return x in self.indices

# Example usage and test
if __name__ == "__main__":
    monotonic_stack = MonotonicStack()
    
    # Push elements onto the stack
    monotonic_stack.push(5)
    monotonic_stack.push(10)
    monotonic_stack.push(15)
    monotonic_stack.push(3)
    monotonic_stack.push(7)
    monotonic_stack.push(2)
    
    # Print the top element of the stack
    print("Top element:", monotonic_stack.top())
    
    # Check if an element exists in the stack
    print("Contains 10?", monotonic_stack.contains(10))
    print("Contains 6?", monotonic_stack.contains(6))
    
    # Pop elements from the stack
    print("Popped element:", monotonic_stack.pop())
    print("Popped element:", monotonic_stack.pop())
    print("Popped element:", monotonic_stack.pop())