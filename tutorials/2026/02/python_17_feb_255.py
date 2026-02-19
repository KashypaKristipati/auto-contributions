class UnionFind:
    def __init__(self, n):
        # Initialize parent array where each element is initially itself
        self.parent = list(range(n))

    def find(self, x):
        # If x is not the root of its set, find the root and make x's root equal to it
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find the roots of x and y
        root_x = self.find(x)
        root_y = self.find(y)

        # If the roots are different, merge them by making one root's parent equal to the other's
        if root_x != root_y:
            self.parent[root_x] = root_y

# Example usage
if __name__ == "__main__":
    # Create a union find object with 5 elements
    uf = UnionFind(5)

    # Initialize some groups (connected components)
    uf.parent[0] = 0
    uf.parent[1] = 0
    uf.parent[2] = 1
    uf.parent[3] = 1
    uf.parent[4] = 2

    print("Initial Group Structure:")
    for i in range(5):
        print(f"{i}: {uf.find(i)}")

    # Merge some groups (connected components)
    uf.union(0, 1)
    uf.union(1, 3)

    print("\nAfter Merging Some Groups:")
    for i in range(5):
        print(f"{i}: {uf.find(i)}")

    # Check that the group structure is correct after merging
    assert uf.find(0) == uf.find(1) == uf.find(3)
    assert uf.find(4) == 4

    # Create another union find object with 5 elements
    uf = UnionFind(5)

    # Initialize some groups (connected components)
    uf.parent[0] = 0
    uf.parent[1] = 0
    uf.parent[2] = 1
    uf.parent[3] = 1
    uf.parent[4] = 2

    print("\n\nAfter Reinitializing Groups:")
    for i in range(5):
        print(f"{i}: {uf.find(i)}")

    # Merge some groups (connected components)
    uf.union(0, 1)

    # Check that the group structure is correct after merging
    assert uf.find(0) == uf.find(1)
    assert uf.find(2) == 2
    assert uf.find(3) == 3
    assert uf.find(4) == 4