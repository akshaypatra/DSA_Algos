'''

1346. Check If N and Its Double Exist
Solved
Easy
Topics
Companies
Hint
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
 

Constraints:

2 <= arr.length <= 500
-103 <= arr[i] <= 103

'''

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        value_to_index_map = {value: index for index, value in enumerate(arr)}
      
        # Iterate through each value in the array.
        for index, value in enumerate(arr):
            # Check if there is a value that is double the current value
            # and ensure that it is not the same instance as the current value.
            if (value * 2 in value_to_index_map) and (value_to_index_map[value * 2] != index):
                return True  # We found a pair where one value is double the other.
      
        # Return False if no pairs were found where one value is double the other.
        return False