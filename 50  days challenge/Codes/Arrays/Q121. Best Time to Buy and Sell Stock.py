'''

121. Best Time to Buy and Sell Stock
Solved
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #bruteforce solution (time limit exceeded)

        '''

        # 198 / 212 testcases passed

        if len(prices)==1:
            return 0

        res=[]
        for i in range(len(prices)-1):
            profit=[]
            for j in range(i+1,len(prices)):
                if prices[j]>prices[i]:
                    profit.append(prices[j]-prices[i])
                    continue
                else:
                    profit.append(0)
            res.append(max(profit))
        return max(res)

        '''

        '''

        # Bruteforce Solution 2 

        if len(prices)==1:
            return 0

        res=[]
        for i in range(len(prices)-1):
            if max(prices[i+1:])<=prices[i]:
                res.append(0)

            else:
                res.append(max(prices[i+1:])-prices[i])

        return max(res)
        
        '''

        #Solution 3 Greedy approach O(n)

        buy=prices[0]
        res=0

        for i in range(1,len(prices)):
            profit=prices[i]-buy
            res=max(res,profit)
            buy=min(buy,prices[i])
        
        return res







                
