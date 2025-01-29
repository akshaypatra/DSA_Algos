'''

684. Redundant Connection
Solved
Medium

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.

'''

# Union find 
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        -> finding root parent
        -> if edges=node (contains cycle)

        '''
        N=len(edges)
        par=[i for i in range(N+1)] # ith node->parent(1-n)
        rank=[1]* (N+1)

        def find(n):
            if n != par[n]:
                par[n]=find(par[n])
            return par[n]



        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1==p2:
                return False

            # Union by rank

            if rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]
            
            return True
        

        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]