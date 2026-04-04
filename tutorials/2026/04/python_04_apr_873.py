class TrieNode:
    # Initialize the node with an empty dictionary to store children and a flag for end of word
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    # Initialize the trie with a root node
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                # Create a new node if it does not exist
                node.children[char] = TrieNode()
            node = node.children[char]
        # Mark the end of the word
        node.end_of_word = True

    # Search for a word in the trie
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

    # Check if a prefix exists in the trie
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Create a new trie
trie = Trie()

# Insert words into the trie
words = ["apple", "banana", "appetizer"]
for word in words:
    trie.insert(word)

# Search for words in the trie
print(trie.search("apple"))  # Output: True
print(trie.search("appetizer"))  # Output: True
print(trie.search("grape"))  # Output: False

# Check prefixes in the trie
print(trie.starts_with("app"))  # Output: True
print(trie.starts_with("gra"))  # Output: False