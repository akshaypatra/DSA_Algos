'''

1462. Course Schedule IV
Solved
Medium

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.

 

Example 1:


Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.
Example 2:

Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.
Example 3:


Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]


'''

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        '''
        def dfs(d,topic,val,visited):

            if topic not in d:
                return False
            if val in d[topic]:
                return True
            for i in d[topic]:
                if i not in visited:
                    visited.add(i)  # Mark as visited
                    if dfs(d, i, val, visited):
                        return True
            return False
            
        
        d={} # prerequisite ->  topic
        for i, j in prerequisites:
            if i not in d:
                d[i] = []
            d[i].append(j)
            
        res = []
        for i, j in queries:
            res.append(dfs(d, i, j, set())) 


        return res
        '''

        
        adj = defaultdict(list)
        for prereq,crs in prerequisites:
            adj[crs].append(prereq)

        
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs]=set()
                for prereq in adj[crs]:
                    prereqMap[crs] |= dfs(prereq) #Union
            
                prereqMap[crs].add(crs)
            return prereqMap[crs]

        prereqMap={} # map crs-> hashset of indirect prereqs

        for crs in range(numCourses):
            dfs(crs)
        
        res=[]
        for u,v in queries:
            res.append(u in prereqMap[v])

        return res
        

        



