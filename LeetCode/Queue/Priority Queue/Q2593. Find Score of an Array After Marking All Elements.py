'''

2593. Find Score of an Array After Marking All Elements
Solved
Medium
Topics
Companies
Hint
You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:

Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
Add the value of the chosen integer to score.
Mark the chosen element and its two adjacent elements if they exist.
Repeat until all the array elements are marked.
Return the score you get after applying the above algorithm.

 

Example 1:

Input: nums = [2,1,3,4,5,2]
Output: 7
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
- 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
- 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
Our score is 1 + 2 + 4 = 7.
Example 2:

Input: nums = [2,3,5,1,3,2]
Output: 5
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,3,5,1,3,2].
- 2 is the smallest unmarked element, since there are two of them, we choose the left-most one, so we mark the one at index 0 and its right adjacent element: [2,3,5,1,3,2].
- 2 is the only remaining unmarked element, so we mark it: [2,3,5,1,3,2].
Our score is 1 + 2 + 2 = 5.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106


'''

class Solution:
    def findScore(self, nums: List[int]) -> int:
        # Calculate the length of the input list.
        length = len(nums)
      
        # Initialize a visited list to keep track of elements that have been added to the score.
        visited = [False] * length
      
        # Create a priority queue with pairs (value, index) for each number in nums.
        priority_queue = [(value, index) for index, value in enumerate(nums)]
        heapify(priority_queue)  # Transform list into a heap, in-place, in linear time.
      
        # Initialize the answer to 0.
        score = 0
      
        # Process the queue until it's empty.
        while priority_queue:
            # Pop the smallest item from the heap, increasing the score by its value.
            value, index = heappop(priority_queue)
            score += value
            visited[index] = True  # Mark the current index as visited.
          
            # Mark the neighbors of the current index as visited.
            for neighbor in (index - 1, index + 1):
                if 0 <= neighbor < length:
                    visited[neighbor] = True
          
            # Remove all elements from the heap whose indices have been visited.
            while priority_queue and visited[priority_queue[0][1]]:
                heappop(priority_queue)
      
        # Return the calculated score.
        return score