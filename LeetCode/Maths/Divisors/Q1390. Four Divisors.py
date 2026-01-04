'''
1390. Four Divisors
Solved
Medium

Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

 

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
Example 2:

Input: nums = [21,21]
Output: 64
Example 3:

Input: nums = [1,2,3,4,5]
Output: 0
 

Constraints:

1 <= nums.length <= 104
1 <= nums[i] <= 105
'''



# Note :

'''
limit = n ** 0.5
We only check divisors up to √n.

👉 Why?
If i divides n, then n // i is also a divisor.
So divisors come in pairs.

Example for n = 16:

1 × 16

2 × 8

4 × 4 (same divisor)
'''

class Solution:
    def get_divisors(self, n):

        divisors = []
        limit = n ** 0.5
        i = 1
        while(i <= limit):

            if(n % i == 0):
                divisors.append(i)
                
                poss_div = n//i
                if(poss_div != i):
                    divisors.append(poss_div)

            i += 1
        
        return divisors
    
    def sumFourDivisors(self, nums: list[int]) -> int:
        
        ans = 0
        for num in nums:
            divisors = self.get_divisors(num)

            if(len(divisors) == 4):
                ans += sum(divisors)
        
        return ans
        