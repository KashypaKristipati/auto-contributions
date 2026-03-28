# Heap Operations in Python

import heapq

def create_min_heap(arr):
    # Create a min heap using the built-in heapq module's heapify function
    heapq.heapify(arr)
    return arr

def insert_into_heap(heap, element):
    # Insert an element into the min heap
    # The element is added to the end of the heap
    heapq.heappush(heap, element)

def delete_from_heap(heap):
    # Delete the minimum element from the min heap
    # The smallest element is removed and returned
    return heapq.heappop(heap)

def heapify_array(arr):
    # Convert an array into a min heap using the heapify function
    # This function rearranges the elements to maintain the heap property
    for i in range(len(arr) // 2 - 1, -1, -1):
        _heapify_helper(arr, i)

def _heapify_helper(arr, i):
    # Recursively rearrange elements to maintain the heap property
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < len(arr) and arr[left] < arr[smallest]:
        smallest = left

    if right < len(arr) and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        _heapify_helper(arr, smallest)

def print_heap(heap):
    # Print the elements of the min heap
    for element in heap:
        print(element, end=' ')

# Create a sample array
arr = [12, 11, 13, 5, 6, 7]

print("Original Array:", arr)
create_min_heap(arr)

print("Min Heap:", end=' ')
heapify_array([0])
insert_into_heap(heap, 4)
insert_into_heap(heap, 2)
insert_into_heap(heap, 1)
insert_into_heap(heap, -3)
insert_into_heap(heap, 10)
print_heap(heap) # Min heap: 1 2 -3 4 5 6 7 10 11 12 13