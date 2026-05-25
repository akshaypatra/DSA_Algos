'''
1871. Jump Game VII
Solved
Medium

You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

 

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.
Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
 

Constraints:

2 <= s.length <= 105
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length
'''
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:


        '''
        Approach 1 : using Queue (BFS) -> (TLE)

        -> add the positions that are reachable and valid
        -> traverse the next position in queue and repeat the above .

        TC : O(n*(maxJump-minJump))
        '''


        # q=deque()
        # q.append(0)
        # i=0
        # while q and i<len(s):
        #     i=q.popleft()
        #     for j in range(i+minJump,i+maxJump+1):
        #         if j<len(s) and s[j]=='0':
        #             if j==len(s)-1:
        #                 return True
        #             q.append(j)

        # return False


        '''
        Approach 2 : Optimization -> Scan from Farthest 

        The optimization is:

            Track the farthest index already explored.
            Never scan the same range twice
        '''

        n = len(s)

        q = deque([0])

        farthest = 0

        while q:

            i = q.popleft()

            start = max(i + minJump, farthest + 1)
            end = min(i + maxJump, n - 1)

            for j in range(start, end + 1):

                if s[j] == '0':

                    if j == n - 1:
                        return True

                    q.append(j)

            farthest = end

        return n == 1
                

        




