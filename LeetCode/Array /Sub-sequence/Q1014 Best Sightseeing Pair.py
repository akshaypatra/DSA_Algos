'''

1014. Best Sightseeing Pair
Solved
Medium
Topics
Companies
Hint
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

 

Example 1:

Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
Example 2:

Input: values = [1,2]
Output: 2
 

Constraints:

2 <= values.length <= 5 * 104
1 <= values[i] <= 1000

'''

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0  # Initialize the maximum score to zero
        max_value_plus_index = values[0]  # Initialize to the first value plus its index (0)

        # Iterate over the array, starting from the second element (index 1)
        for i in range(1, len(values)):
            # Update the max score using the current value and the best previous value plus index found
            max_score = max(max_score, values[i] - i + max_value_plus_index)
            # Update the max_value_plus_index with the maximum of the current and the previous
            # while accounting for the increasing index
            max_value_plus_index = max(max_value_plus_index, values[i] + i)

        # Return the maximum score found for any sightseeing pair
        return max_score