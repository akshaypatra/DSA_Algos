'''

135. Candy
Solved
Hard

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104

'''

class Solution:
    def candy(self, ratings: List[int]) -> int:
         # Length of the ratings list
        num_children = len(ratings)
      
        # Initialize lists to represent the minimum candies for each child from left and right perspectives
        candies_from_left = [1] * num_children
        candies_from_right = [1] * num_children
      
        # Calculating the minimum candies required from the left perspective
        for i in range(1, num_children):
            if ratings[i] > ratings[i - 1]:
                candies_from_left[i] = candies_from_left[i - 1] + 1
      
        # Calculating the minimum candies required from the right perspective
        for i in range(num_children - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies_from_right[i] = candies_from_right[i + 1] + 1
      
        # Sum the max number of candies required from both perspectives for each child
        # to ensure all conditions are met
        total_candies = sum(max(candies_left, candies_right) for candies_left, candies_right in zip(candies_from_left, candies_from_right))
      
        return total_candies