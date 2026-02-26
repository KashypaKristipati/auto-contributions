# Heap Operations in Python

# Importing the heapq module for heap operations
import heapq

# Creating a min heap
def create_min_heap():
    # Using the heapify function from the heapq module to create a min heap
    # This function rearranges the elements in the list to create a heap
    min_heap = [4, 2, 9, 6, 5, 1, 8, 3, 7]
    heapq.heapify(min_heap)
    return min_heap

# Extracting the minimum element from the heap
def extract_min(heap):
    # Using the heappop function from the heapq module to extract the minimum element
    # This function removes and returns the smallest element from the heap
    return heapq.heappop(heap)

# Inserting an element into the heap
def insert_min(heap, element):
    # Using the heappush function from the heapq module to insert an element into the heap
    # This function adds an element to the heap
    heapq.heappush(heap, element)

# Heap operations
def heap_operations():
    # Creating a min heap
    min_heap = create_min_heap()
    print("Min Heap:", min_heap)

    # Extracting the minimum element
    min_element = extract_min(min_heap)
    print("Minimum Element:", min_element)

    # Inserting an element into the heap
    insert_min(min_heap, 10)
    print("Heap after insertion:", min_heap)

    # Extracting the minimum element again
    min_element = extract_min(min_heap)
    print("Minimum Element after second extraction:", min_element)

# Running the heap operations
heap_operations()
```

# Running the code
# Create a new python file, copy the above code and run it