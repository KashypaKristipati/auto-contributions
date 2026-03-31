def compute_prefix_function(pattern):
    # Initialize the prefix function with zeros
    m = len(pattern)
    pi = [0] * m
    
    j = 0
    for i in range(1, m):
        # If the current character doesn't match the prefix character,
        # then use the value at index j to move forward in the pattern
        while j > 0 and pattern[j] != pattern[i]:
            j = pi[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        pi[i] = j
    
    return pi

def kmp_search(text, pattern):
    # Compute the prefix function for the pattern
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    
    n = len(text)
    j = 0
    
    for i in range(n):
        # If the current character of the text matches the current character of the pattern,
        # then move forward in both the text and the pattern
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        
        if text[i] == pattern[j]:
            j += 1
        
        # If we've reached the end of the pattern, then a match has been found
        if j == m:
            print(f"Found match at position {i - j + 1}")
            j = pi[j - 1]
    
    return None

# Example usage:
text = "abxabcabcabcd"
pattern = "abc"

kmp_search(text, pattern)