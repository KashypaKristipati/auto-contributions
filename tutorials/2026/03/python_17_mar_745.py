# KMP String Search Algorithm in Python
=====================================================

### Overview

The Knuth-Morris-Pratt (KMP) algorithm is a linear-time string searching algorithm that uses the observation that when a mismatch occurs, we don't have to start from the beginning of the text.

### Code

```python
def compute_prefix_function(pattern):
    """
    Compute prefix function for KMP algorithm.
    
    The prefix function is used to store information about how many characters 
    in the pattern are yet to be matched when a mismatch occurs.
    """
    # Initialize prefix function array with zeros
    prefix = [0] * len(pattern)
    j = 0
    
    # Compute prefix function values
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        
        if pattern[i] == pattern[j]:
            j += 1
        
        # Update prefix function value
        prefix[i] = j
    
    return prefix


def kmp_search(text, pattern):
    """
    Perform KMP search on the given text for the pattern.
    
    Returns the starting index of the first occurrence of the pattern in 
    the text. If no occurrence is found, returns -1.
    """
    # Compute prefix function values
    prefix = compute_prefix_function(pattern)
    
    j = 0  # Index into pattern
    i = 0  # Index into text
    
    while i < len(text):
        if j > 0 and text[i] == pattern[j]:
            j += 1
        
        # If we've matched the entire pattern, return starting index
        if j == len(pattern):
            return i - j + 1
        
        # If there's a mismatch, try to recover by resetting j
        elif text[i] != pattern[j]:
            if j > 0:
                j = prefix[j - 1]
            else:
                i += 1
    
    # If no occurrence found, return -1
    return -1


# Example usage:
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABAB"

    result = kmp_search(text, pattern)
    
    if result != -1:
        print("Pattern found at index:", result)
    else:
        print("Pattern not found.")