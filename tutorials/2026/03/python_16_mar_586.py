# Sliding Window Technique in Python
=====================================

The sliding window technique is an efficient algorithmic strategy used to solve problems that require examining a subset of data from the entire dataset. This approach is particularly useful when dealing with large datasets or when the problem requires finding specific patterns within the data.

### Problem Statement:
Given a string `s` and an integer `k`, find all occurrences of a substring of length `k` in `s`.

### Solution:

```python
def find_substring(s, k):
    """
    Find all occurrences of a substring of length k in s.
    
    Parameters:
    s (str): The input string.
    k (int): The length of the substring to find.
    
    Returns:
    list: A list of tuples containing the start and end indices of each occurrence.
    """
    # Initialize an empty list to store the occurrences
    occurrences = []
    
    # Calculate the maximum possible start index for the window
    max_start_index = len(s) - k + 1
    
    # Iterate over all possible start indices for the window
    for i in range(max_start_index):
        # Extract the substring of length k starting at the current index
        window = s[i:i+k]
        
        # Check if the substring is equal to a fixed string (in this case, "abc")
        # If it is, add the start and end indices to the occurrences list
        if window == "abc":
            occurrences.append((i, i + k - 1))
    
    return occurrences

# Test the function with an example
s = "abxabcaby"
k = 3
print(find_substring(s, k))  # Output: [(0, 2), (4, 6)]