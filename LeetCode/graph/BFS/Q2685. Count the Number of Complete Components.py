'''
2685. Count the Number of Complete Components
Solved
Medium

You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.

 

Example 1:



Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that all of the components of this graph are complete.
Example 2:



Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.

'''

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        # Build adjacency list
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def is_complete_component(node):
            """ Checks if the component starting from 'node' is a complete graph. """
            queue = [node]
            component = set([node])
            visited.add(node)

            # BFS to find all nodes in the connected component
            while queue:
                curr = queue.pop()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        component.add(neighbor)

            # Check if it's a complete graph
            size = len(component)
            for v in component:
                if len(graph[v]) != size - 1:  # Every node should be connected to (size-1) other nodes
                    return False
            return True

        complete_components = 0

        # Process all nodes
        for i in range(n):
            if i in visited:
                continue
            if i not in graph:  # Isolated node
                complete_components += 1
                visited.add(i)
            elif is_complete_component(i):  # Check if it's a complete subgraph
                complete_components += 1

        return complete_components


                
