'''

386. Lexicographical Numbers
Solved
Medium

Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 

Constraints:

1 <= n <= 5 * 104

'''

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        '''
        tackled the problem digit by digit 
        '''

            # def dfs(digit):
            #     if digit=="0":
            #         return 

            #     for i in range(10):
            #         s=digit+str(i)
 
            #         if int(s)<=n:
            #             if s=="0":
            #                 continue
            #             res.append(int(s))
            #             dfs(str(s))
            #         else:
            #             break

            # res=[]
            # dfs("")
            
            # return res


        '''
        Optimized version
        '''
        def dfs(curr):
            if curr > n:
                return
            res.append(curr)
            for i in range(10):
                next_num = curr * 10 + i
                if next_num > n:
                    break
                dfs(next_num)

        res = []
        for i in range(1, 10):
            dfs(i)
        return res
