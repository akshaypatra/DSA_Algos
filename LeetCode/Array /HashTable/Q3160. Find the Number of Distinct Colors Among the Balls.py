'''

3160. Find the Number of Distinct Colors Among the Balls
Solved
Medium

You are given an integer limit and a 2D array queries of size n x 2.

There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.

Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.

Note that when answering a query, lack of a color will not be considered as a color.

 

Example 1:

Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]

Output: [1,2,2,3]

Explanation:



After query 0, ball 1 has color 4.
After query 1, ball 1 has color 4, and ball 2 has color 5.
After query 2, ball 1 has color 3, and ball 2 has color 5.
After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color 4.
Example 2:

Input: limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]

Output: [1,2,2,3,4]

Explanation:



After query 0, ball 0 has color 1.
After query 1, ball 0 has color 1, and ball 1 has color 2.
After query 2, ball 0 has color 1, and balls 1 and 2 have color 2.
After query 3, ball 0 has color 1, balls 1 and 2 have color 2, and ball 3 has color 4.
After query 4, ball 0 has color 1, balls 1 and 2 have color 2, ball 3 has color 4, and ball 4 has color 5.
 

Constraints:

1 <= limit <= 109
1 <= n == queries.length <= 105
queries[i].length == 2
0 <= queries[i][0] <= limit
1 <= queries[i][1] <= 109

'''


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:


        # Dictionary to store the mapping of 'x' -> 'y' values
        mapping = {}
      
        # Counter to keep track of the frequency of each 'y' value
        frequency_counter = Counter()
      
        # List to store results
        results = []
      
        # Process each query which is a pair (x, y)
        for x, y in queries:
            # Increase the counter for 'y'
            frequency_counter[y] += 1
          
            # If 'x' already exists in the mapping, update the counter for the old 'y' value
            if x in mapping:
                old_y = mapping[x]
                frequency_counter[old_y] -= 1
              
                # Remove entry from counter if the frequency becomes zero
                if frequency_counter[old_y] == 0:
                    frequency_counter.pop(old_y)
          
            # Update the mapping with the new 'y' value for 'x'
            mapping[x] = y
          
            # Append the number of unique 'y' values to the results
            results.append(len(frequency_counter))
      
        return results




        '''
        # First Try : Not working

        e_color = {}  # Mapping of element -> color
        color_f = defaultdict(int)  # Mapping of color -> frequency
        color_count = 0  # Tracks unique color IDs
        res = []

        def helper(x):
            """Assigns a new color to the ball if necessary."""
            nonlocal color_count
            if x in e_color:  
                color_f[e_color[x]] -= 1  # Reduce count of old color
                if color_f[e_color[x]] == 0:
                    del color_f[e_color[x]]  # Remove empty colors
            e_color[x] = color_count
            color_f[color_count] += 1

        for i, j in queries:
            if j not in e_color:
                color_count += 1  # Assign new color
                helper(j)
            else:
                if color_f[e_color[j]] >= limit:  # If color is at limit, assign a new color
                    color_count += 1
                    helper(j)
                else:
                    color_f[e_color[j]] += 1  # Increment the count of the existing color
            
            # Count distinct colors
            res.append(len(color_f))

        return res

        '''
                    




















  

                    




                    
                

            
            
                

        


