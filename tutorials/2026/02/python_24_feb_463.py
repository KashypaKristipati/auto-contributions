# Monotonic Stack Implementation in Python

class MonotonicStack:
    # Initialize the stack and the smallest and largest elements seen so far
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.max_stack = []

    # Push element onto the stack
    def push(self, x):
        # Add element to the main stack
        self.stack.append(x)
        
        # If the min stack is empty or the element is smaller than the current min
        if not self.min_stack or x <= self.min_stack[-1][0]:
            # Update the min stack
            self.min_stack.append((x, self.min_stack[-1][1] if self.min_stack else float('-inf')))
        
        # If the max stack is empty or the element is larger than the current max
        if not self.max_stack or x >= self.max_stack[-1][0]:
            # Update the max stack
            self.max_stack.append((x, self.max_stack[-1][1] if self.max_stack else float('inf')))

    # Pop element from the stack
    def pop(self):
        # Check if the stack is not empty
        if self.stack:
            # Remove the last element from the main stack
            x = self.stack.pop()
            
            # If the removed element is equal to the current min
            if x == self.min_stack[-1][0]:
                # Remove the last element from the min stack
                self.min_stack.pop()
            # If the removed element is equal to the current max
            elif x == self.max_stack[-1][0]:
                # Remove the last element from the max stack
                self.max_stack.pop()
            return x
        return None

# Example usage
stack = MonotonicStack()
stack.push(5)
stack.push(3)
stack.push(7)
stack.push(2)
stack.push(10)
stack.push(8)

# Print the monotonic stack
while stack.stack:
    x = stack.pop()
    print(x)

# Print the monotonic stack
while stack.min_stack:
    x, min_val = stack.pop_min()
    print(f'Min: {x}, Min Value: {min_val}')

# Print the monotonic stack
while stack.max_stack:
    x, max_val = stack.pop_max()
    print(f'Max: {x}, Max Value: {max_val}')