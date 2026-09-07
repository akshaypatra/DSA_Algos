'''
781. Rabbits in Forest
Solved
Medium

There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits that could be in the forest.

 

Example 1:

Input: answers = [1,1,2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit that answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
Example 2:

Input: answers = [10,10,10]
Output: 11
 

Constraints:

1 <= answers.length <= 1000
0 <= answers[i] < 1000

'''

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Count the occurrences of each answer
        answer_counter = Counter(answers)
      
        # Initialize total number of rabbits reported
        total_rabbits = 0
      
        # Iterate through each unique answer (number_of_other_rabbits) and its count
        for number_of_other_rabbits, count in answer_counter.items():
            # Each rabbit with the same answer (number_of_other_rabbits) forms a group.
            # The size of each group is number_of_other_rabbits + 1 (including itself).
            group_size = number_of_other_rabbits + 1
          
            # Calculate the number of full groups (possibly partial for the last group)
            # by dividing the count of rabbits by the group size and rounding up.
            # This gives the number of groups where each rabbit reports
            # number_of_other_rabbits other rabbits with the same color.
            number_of_groups = math.ceil(count / group_size)
          
            # Add to the total number of rabbits by multiplying the number of groups
            # by the size of the group.
            total_rabbits += number_of_groups * group_size
      
        # Return the total number of rabbits reported
        return total_rabbits