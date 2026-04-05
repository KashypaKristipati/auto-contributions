# KMP String Search Algorithm
def compute_prefix_function(pattern):
    # Initialize the prefix function with zeros
    m = len(pattern)
    pi = [0] * m
    
    # Compute the prefix function values
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]:
            j = pi[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        pi[i] = j
    
    return pi

def kmp_search(text, pattern):
    # Compute the prefix function values for the pattern
    pi = compute_prefix_function(pattern)
    
    # Initialize the search variables
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
                j = pi[j - 1]
            else:
                i += 1
    
    # If the pattern is not found, return -1
    return -1

# Test the KMP algorithm
text = "ABCDABCD"
pattern = "ABCDAB"
result = kmp_search(text, pattern)
if result != -1:
    print(f"Pattern found at index {result}")
else:
    print("Pattern not found in the text")