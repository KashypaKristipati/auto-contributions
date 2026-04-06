class UnionFind:
    def __init__(self, n):
        # Initialize the parent array, where each element is initially itself
        self.parent = list(range(n))
    
    def find(self, x):
        # If x is not its own parent (i.e., it's not in a set of its own), 
        # then find(x) must return the root of that set
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        # Find the roots of the sets that x and y belong to
        root_x = self.find(x)
        root_y = self.find(y)
        
        # If the two roots are not the same, then merge the two sets
        if root_x != root_y:
            self.parent[root_x] = root_y

# Create a UnionFind object with 5 elements
uf = UnionFind(5)

# Perform some unions and find operations
print("Initial state:")
for i in range(5):
    print(f"{i} is in set {uf.find(i)}")

# Merge two sets
uf.union(0, 1)
print("\nAfter union(0,1):")
for i in range(5):
    print(f"{i} is in set {uf.find(i)}")

# Merge another two sets
uf.union(2, 3)
print("\nAfter union(2,3):")
for i in range(5):
    print(f"{i} is in set {uf.find(i)}")