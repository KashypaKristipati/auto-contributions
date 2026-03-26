#!/usr/bin/env python
# KMP String Search Algorithm in Python

def compute_prefix_function(pattern):
    # Initialize prefix function array with zeros
    m = len(pattern)
    pi = [0] * m
    
    # Compute prefix function values
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]:
            j = pi[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        pi[i] = j
    
    return pi

def kmp_search(text, pattern):
    # Compute prefix function for the pattern
    pi = compute_prefix_function(pattern)
    
    # Initialize pointers
    m = len(pattern)
    n = len(text)
    i = j = 0
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            print("Pattern found at index", i - j)
            j = pi[j - 1]
        
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = pi[j - 1]
            else:
                i += 1
    
    return "Pattern not found"

# Test the KMP algorithm
text = "ABCDABCDAB"
pattern = "ABCDAB"
print(kmp_search(text, pattern))