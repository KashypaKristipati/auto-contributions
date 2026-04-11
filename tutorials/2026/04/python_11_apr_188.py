# Heap Operations in Python
# A Python implementation of the heap data structure.

import heapq

class Heap:
    def __init__(self):
        # Initialize an empty list to act as our heap.
        self.heap = []

    def parent(self, i):
        # Calculate the index of the parent node.
        return (i - 1) // 2

    def left_child(self, i):
        # Calculate the index of the left child node.
        return 2 * i + 1

    def right_child(self, i):
        # Calculate the index of the right child node.
        return 2 * i + 2

    def insert(self, value):
        # Insert a new value into the heap.
        heapq.heappush(self.heap, value)

    def delete_min(self):
        # Delete and return the minimum value from the heap.
        if not self.is_empty():
            min_value = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.heapify(0)
            return min_value
        else:
            raise ValueError("Heap is empty")

    def heapify(self, i):
        # Heapify the subtree rooted at index i.
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)

    def swap(self, i, j):
        # Swap the values at indices i and j.
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_empty(self):
        # Check if the heap is empty.
        return len(self.heap) == 0

# Example usage of a heap.
if __name__ == "__main__":
    heap = Heap()
    heap.insert(10)
    heap.insert(20)
    heap.insert(15)

    print("Heap elements:", heap.heap)
    print("Deleted minimum value:", heap.delete_min())
    print("Heap after deletion:", heap.heap)