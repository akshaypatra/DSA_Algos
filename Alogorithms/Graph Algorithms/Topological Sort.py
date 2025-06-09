'''
Topological Sorting of a Directed Acyclic Graph (DAG) is a linear ordering of its vertices such that for every directed edge u → v, vertex u comes before v in the ordering.

🧠 Intuition Behind DFS-Based Topological Sort

In DFS:

-> We go deep in the graph before backtracking.
-> Once we finish visiting all descendants of a node, we record that node (usually by adding it to a stack or list).
-> Since we visit all the dependencies before the node itself, the reverse of the finishing order gives the topological sort.


----------------------------------------------------------------------
   Property	          |         Description                          |
----------------------------------------------------------------------                   
-> Applicable To	  |       Directed Acyclic Graph (DAG) only      |
-> Time Complexity	  |       O(V + E) where V = vertices, E = edges |
-> Space Complexity   |       O(V) for visited and recursion stack   |
---------------------------------------------------------------------- 

'''

from collections import defaultdict

class Solution:
    def topologicalSort(self, numVertices: int, edges: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        visited = [False] * numVertices
        result = []

        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            result.append(node)

        for i in range(numVertices):
            if not visited[i]:
                dfs(i)

        result.reverse()
        return result


numVertices = 6
edges = [
    [5, 2],
    [5, 0],
    [4, 0],
    [4, 1],
    [2, 3],
    [3, 1]
]

sol = Solution()
print(sol.topologicalSort(numVertices, edges))
