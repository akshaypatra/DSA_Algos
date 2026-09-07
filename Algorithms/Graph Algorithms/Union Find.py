'''
Union-Find (Disjoint Set Union) 
Union-Find (also called Disjoint Set Union, DSU) is a data structure used to keep track of elements partitioned into disjoint (non-overlapping) sets and efficiently supports two operations:

📌 Operations:
Find(x) → returns the representative (or root parent) of the set containing x.

Union(x, y) → merges the sets containing x and y.

🧠 Optimization Techniques:

-> Path Compression: Speeds up find() by making every node on the path point directly to the root.
-> Union by Rank / Size: Always attach the smaller tree under the root of the larger tree.

Time Complexity : O(log n)
Space Complexity : O(n)

'''

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size  # Rank (can also use size)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return  # already connected

        # Union by rank
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1


'''
# Usage :

uf = UnionFind(10)
uf.union(1, 2)
uf.union(2, 3)

print(uf.find(3))  # Output: 1 (or the root of the set that includes 1, 2, 3)

'''

#  Related Question : 1061. Lexicographically Smallest Equivalent String