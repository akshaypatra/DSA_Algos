'''
The K-Sum technique is a recursive way to solve problems like:

2 Sum
3 Sum
4 Sum
5 Sum
...
K Sum

Instead of writing a separate solution for each, you write one recursive function that reduces K-Sum → (K-1)-Sum → ... → 2-Sum.

Instead of thinking:
    Find 4 numbers that sum to target.
Think:
    Fix one number, then find 3 numbers that sum to the remaining target.
    

Recursive tree of 4 Sum :

KSum(4)

├── choose a
│   └── KSum(3)
│       ├── choose b
│       │   └── KSum(2)
│       │       └── two pointers
│       ├── choose c
│       │   └── KSum(2)
│       └── ...
│
├── choose next a
│   └── KSum(3)
│
└── ...
'''


# COde :

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        A generic K Sum code having a recursion technique
        '''
        nums.sort()
        res,quad = [],[]

        def KSum(k,start,target):

            if k != 2:
                for i in range(start,len(nums)-k+1):
                    if i>start and nums[i]==nums[i-1]:
                        continue
                    quad.append(nums[i])
                    KSum(k-1,i+1,target-nums[i])
                    quad.pop()
                return 
            
            # Base case 2 sum technique (avoiding duplicate)
            l,r = start,len(nums)-1

            while l<r:
                if nums[l]+nums[r] > target :
                    r-=1
                elif nums[l]+nums[r] < target :
                    l+=1
                else :
                    res.append(quad + [nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1

        KSum(4,0,target)
        return res


