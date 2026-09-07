'''

1534. Count Good Triplets
Solved
Easy

Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.

 

Example 1:

Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
Example 2:

Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.
 

Constraints:

3 <= arr.length <= 100
0 <= arr[i] <= 1000
0 <= a, b, c <= 1000

'''

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        '''
        BruteForce Solution :
        O(n^3) Solution 

        '''

        # count=0
        # for i in range(len(arr)-2):
        #     for j in range(i+1,len(arr)-1):
                
        #         for k in range(j+1,len(arr)):
        #             if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i] - arr[k]) <= c:
        #                 count+=1
        # return count

        '''
        Slight optimization before last loop runs
        -> O(n^3)

        '''

        # count=0
        # for i in range(len(arr)-2):
        #     for j in range(i+1,len(arr)-1):
        #         if abs(arr[i]-arr[j])<=a:
        #             for k in range(j+1,len(arr)):
        #                 if  abs(arr[j]-arr[k])<=b and abs(arr[i] - arr[k]) <= c:
        #                     count+=1
        # return count

        '''

        Optimized solution using Prefix Counting

        ->O(n^2)

        '''

        res=0
        N=len(arr)
        prefix_count=[0]*1001 #Prefix counts : prefix_xount[x] -> count of nums <=x

        for j in range(N-1):
            for k in range(j+1,N):
                if abs(arr[j] - arr[k])<=b:
                    # how many values before j where abs condition is met
                    r=min(arr[j]+a,arr[k]+c)
                    l=max(arr[j]-a,arr[k]-c)

                    l=max(l,0)
                    r=min(r,1000)

                    if l<=r:
                        res+=prefix_count[r] - (0 if l==0 else prefix_count[l-1])
            for index in range(arr[j],1001):
                prefix_count[index]+=1
        return res


