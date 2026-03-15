# Trie Data Structure in Python
=====================================

## Introduction

A Trie is a type of data structure that is used to store and retrieve strings. It is also known as a prefix tree because it stores all the strings with common prefixes in a sorted order.

## Implementation

```python
class TrieNode:
    """A node in the Trie data structure."""
    def __init__(self):
        # Initialize an empty dictionary to store child nodes
        self.children = {}
        # Initialize a boolean flag to indicate whether the node represents the end of a word
        self.is_end_of_word = False

class Trie:
    """The Trie data structure."""
    def __init__(self):
        # Initialize the root node of the Trie
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the Trie."""
        current_node = self.root
        for char in word:
            # If the character is not already a child of the current node, add it
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        # Mark the final node as the end of a word
        current_node.is_end_of_word = True

    def search(self, word):
        """Search for a word in the Trie."""
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        # Return True if the final node is marked as the end of a word
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        """Check if there are any words that start with a given prefix."""
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        # If we reach this point, it means the prefix exists in the Trie
        return True

# Example usage:
trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("orange")

print(trie.search("apple"))  # Output: True
print(trie.starts_with("app"))  # Output: True
print(trie.search("grape"))  # Output: False