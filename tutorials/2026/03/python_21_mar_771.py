# knuth_morris_pratt.py
def compute_prefix_function(pattern):
    # Initialize the prefix function with zeros
    prefix = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[j] != pattern[i]:
            j = prefix[j-1]
        if pattern[j] == pattern[i]:
            j += 1
        prefix[i] = j
    return prefix

def knuth_morris_pratt_search(text, pattern):
    # Compute the prefix function for the pattern
    prefix = compute_prefix_function(pattern)
    
    # Initialize the indices for the text and pattern
    m = len(pattern)
    n = len(text)
    i = j = 0
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = prefix[j-1]
            else:
                i += 1
    
    # If no match is found
    return -1

# Test the algorithm
text = "ABCDABCAB"
pattern = "ABC"
index = knuth_morris_pratt_search(text, pattern)
if index != -1:
    print(f"Pattern '{pattern}' found at position {index} in text '{text}'")
else:
    print(f"Pattern '{pattern}' not found in text '{text}'")