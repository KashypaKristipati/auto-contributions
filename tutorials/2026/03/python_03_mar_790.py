import bisect

def binary_search(arr, target):
    # Create a sorted copy of the input array
    sorted_arr = sorted(arr)
    # Use binary search function from the bisect module
    index = bisect.bisect_left(sorted_arr, target)
    # If the target is found, return the index
    if index != len(sorted_arr) and sorted_arr[index] == target:
        return index
    # If the target is not found, return -1
    return -1

def main():
    # Create an unsorted list of integers
    arr = [5, 2, 8, 3, 1, 6, 4]
    # Define the target number to search for
    target = 6
    # Call the binary_search function
    result = binary_search(arr, target)
    # Print the result
    print("Result:", result)

if __name__ == "__main__":
    main()