# Segment Tree Implementation in Python

class SegmentTree:
    def __init__(self, arr):
        """
        Initialize the segment tree with the given array.
        
        :param arr: The input array to be stored in the segment tree.
        """
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # Initialize the segment tree with zeros
        self.build_tree(arr, 0, 0, self.n - 1)

    def build_tree(self, arr, node, start, end):
        """
        Recursively build the segment tree.
        
        :param arr: The input array to be stored in the segment tree.
        :param node: The current node index in the tree.
        :param start: The start index of the current segment.
        :param end: The end index of the current segment.
        """
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            # Recursively build the left and right subtrees
            self.build_tree(arr, 2 * node + 1, start, mid)
            self.build_tree(arr, 2 * node + 2, mid + 1, end)

            # Update the current node with the minimum value from its children
            self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, node, start, end, left, right):
        """
        Query the segment tree to find the minimum sum between a given range.
        
        :param node: The current node index in the tree.
        :param start: The start index of the current segment.
        :param end: The end index of the current segment.
        :param left: The start index of the query range (inclusive).
        :param right: The end index of the query range (inclusive).
        """
        if left > end or right < start:
            return float('inf')  # Return infinity if the range is invalid
        elif left <= start and end <= right:
            return self.tree[node]  # Return the minimum sum from the current node

        mid = (start + end) // 2
        # Recursively query the left and right subtrees
        left_min = self.query(2 * node + 1, start, mid, left, right)
        right_min = self.query(2 * node + 2, mid + 1, end, left, right)

        # Return the minimum sum from the children
        return min(left_min, right_min)

    def update(self, node, start, end, idx, val):
        """
        Update the segment tree with a new value at a given index.
        
        :param node: The current node index in the tree.
        :param start: The start index of the current segment.
        :param end: The end index of the current segment.
        :param idx: The index to update in the array.
        :param val: The new value to update at the given index.
        """
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            # Recursively update the left and right subtrees
            if idx <= mid