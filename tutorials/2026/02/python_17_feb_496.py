# Union-Find Algorithm Implementation in Python

class UnionFind:
    def __init__(self, n):
        """
        Initialize the union-find data structure with n elements.
        
        :param n: Number of elements in the set.
        """
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """
        Find the representative element (root) of the set containing x.
        
        :param x: Element to find the representative for.
        :return: Representative element of the set containing x.
        """
        if self.parent[x] != x:
            # Path compression optimization
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Merge the sets containing x and y into a single set.
        
        :param x: Element to merge with.
        :param y: Element to merge with.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Union by rank
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                # Promotion to reduce the rank of the new representative
                self.rank[root_x] += 1

# Example usage
if __name__ == "__main__":
    uf = UnionFind(6)

    print("Initial set status:")
    for i in range(1, 7):
        print(f"{i}: {uf.find(i)}")

    # Merge sets containing elements 1 and 3
    uf.union(1, 3)
    print("\nAfter merging sets containing 1 and 3:")
    for i in range(1, 7):
        print(f"{i}: {uf.find(i)}")

    # Merge sets containing elements 4 and 5
    uf.union(4, 5)
    print("\nAfter merging sets containing 4 and 5:")
    for i in range(1, 7):
        print(f"{i}: {uf.find(i)}")

    # Check if the sets containing elements 2 and 6 are separate
    print("\nAre sets containing 2 and 6 separate?")
    uf.union(2, 6)
    print(f"Representative of set containing 2: {uf.find(2)}, Representative of set containing 6: {uf.find(6)}")