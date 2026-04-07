# Monotonic Stack Implementation in Python

class MonotonicStack:
    def __init__(self):
        """
        Initialize the monotonic stack with an empty list.
        """
        # We use a list as our underlying data structure for the stack.
        self.stack = []

    def push(self, value):
        """
        Push a new element onto the stack while maintaining monotonic order.

        If the stack is already sorted in ascending or descending order,
        we simply append the new element. Otherwise, we need to compare
        it with elements at the top of the stack and swap if necessary.
        """
        # Check if the stack is empty or not sorted
        if self.is_sorted():
            # Append the new element to the end of the list
            self.stack.append(value)
        else:
            # Compare the new value with the top element of the stack
            top = self.stack[-1]
            if value < top:
                # If the new value is smaller, remove elements from the top
                while self.stack and self.stack[-1] > value:
                    self.stack.pop()
                # Push the new value onto the stack
                self.stack.append(value)
            elif value > top:
                # If the new value is larger, push it onto the stack
                self.stack.append(value)

    def pop(self):
        """
        Remove and return the top element from the stack.

        If the stack is empty or not sorted, this operation may not work correctly.
        """
        if not self.is_sorted():
            raise ValueError("Stack is not sorted")
        # Pop the last element off the list
        return self.stack.pop()

    def is_sorted(self):
        """
        Check if the elements in the stack are sorted in ascending order.

        Returns True if the stack is sorted, False otherwise.
        """
        # Sort a copy of the underlying data structure and compare with the original
        sorted_list = sorted(self.stack)
        return self.stack == sorted_list

# Example usage:
if __name__ == "__main__":
    monotonic_stack = MonotonicStack()
    # Push some elements onto the stack
    for i in range(10):
        monotonic_stack.push(i)

    print("Stack:", monotonic_stack.stack)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Pop some elements off the stack
    for _ in range(5):
        print(monotonic_stack.pop())  # 9, 8, 7, 6, 5

    print("Stack:", monotonic_stack.stack)  # [4, 3, 2, 1, 0]