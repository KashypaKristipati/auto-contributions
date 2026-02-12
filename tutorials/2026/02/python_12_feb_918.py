# Trie Data Structure in Python

class TrieNode:
    # Initialize a new node in the trie with an empty dictionary
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Flag to mark the end of a word

class Trie:
    # Initialize a new trie and add it as a property
    def __init__(self):
        self.root = TrieNode()  # Create the root node

    # Insert a word into the trie
    def insert(self, word):
        current = self.root  # Start at the root node
        for char in word:
            if char not in current.children:  # If the character is not in children
                current.children[char] = TrieNode()  # Create a new child node
            current = current.children[char]  # Move to the child node
        current.is_end_of_word = True  # Mark the end of the word

    # Search for a word in the trie
    def search(self, word):
        current = self.root  # Start at the root node
        for char in word:
            if char not in current.children:  # If the character is not in children
                return False  # The word is not in the trie
            current = current.children[char]  # Move to the child node
        return current.is_end_of_word  # Return whether the word ends at this node

    # Check if a prefix exists in the trie
    def starts_with(self, prefix):
        current = self.root  # Start at the root node
        for char in prefix:
            if char not in current.children:  # If the character is not in children
                return False  # The prefix is not in the trie
            current = current.children[char]  # Move to the child node
        return True  # The prefix exists

    # Run a test case
if __name__ == "__main__":
    trie = Trie()  # Create a new trie

    words = ["apple", "app", "banana", "bat"]
    for word in words:
        trie.insert(word)

    print(trie.search("apple"))  # Output: True
    print(trie.search("ap"))  # Output: False
    print(trie.starts_with("a"))  # Output: True
    print(trie.starts_with("b"))  # Output: False