# Segment Tree Implementation in Python
#==========================================

class SegmentTree:
    def __init__(self, data):
        """
        Initialize the segment tree with the given data.
        
        Args:
            data (list): The input data to be stored in the segment tree.
        """
        # Calculate the size of the segment tree based on the input data
        n = len(data)
        self.size = 1 << (n - 1).bit_length()
        self.tree = [0] * (2 * self.size)

        # Build the segment tree by propagating the data from the leaves
        for i in range(n):
            self.tree[i + self.size] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, pos, val):
        """
        Update the value at the given position in the segment tree.
        
        Args:
            pos (int): The position in the segment tree to be updated.
            val (int): The new value to be stored at the given position.
        """
        # Update the value at the given position
        pos += self.size
        self.tree[pos] = val

        # Propagate the changes to the ancestors
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def query(self, left, right):
        """
        Query the sum of values in the given range of the segment tree.
        
        Args:
            left (int): The starting position of the range.
            right (int): The ending position of the range.
        
        Returns:
            int: The sum of values in the given range.
        """
        # Calculate the sum of values in the given range using the segment tree
        left += self.size
        right += self.size

        # Initialize the sum as zero
        total = 0

        # Propagate the values from the leaves to the ancestors
        while left < right:
            if left % 2 == 1:
                total += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                total += self.tree[right]
            left //= 2
            right //= 2

        return total

# Example usage
if __name__ == "__main__":
    # Create a sample data
    data = [1, 2, 3, 4, 5]
    st = SegmentTree(data)

    # Update the values in the segment tree
    st.update(0, 10)
    st.update(1, 20)
    st.update(2, 30)

    # Query the sum of values in the segment tree
    print("Sum of values in the first two positions:", st.query(0, 2))
    print("Sum of values in the last two positions:", st.query(2, 4))