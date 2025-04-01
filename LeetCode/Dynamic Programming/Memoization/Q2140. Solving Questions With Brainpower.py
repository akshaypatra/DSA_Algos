'''

2140. Solving Questions With Brainpower
Solved
Medium

You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.

 

Example 1:

Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5
Explanation: The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
Example 2:

Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
Output: 7
Explanation: The maximum points can be earned by solving questions 1 and 4.
- Skip question 0
- Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
- Unable to solve questions 2 and 3
- Solve question 4: Earn 5 points
Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.
 

Constraints:

1 <= questions.length <= 105
questions[i].length == 2
1 <= pointsi, brainpoweri <= 105

'''

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:


        '''
        Intuition : Bruteforce

        -recursion(when  val is included)
        -recursion(when val is not included)
        return max(both recursions)

        '''

        # Time Limit Exceeded
        # def helper(index):
        #     if index >= len(questions):
        #         return 0  
        
        #     points, skip = questions[index]  

   
        #     included_points = points + helper(index + skip + 1)

      
        #     not_included_points = helper(index + 1)

        #     return max(included_points, not_included_points)
            
        
        # return helper(0)

        '''

        Using Memoization to optimize the above code

        -> added a cache to store the res of elements that are previously included

        '''
        cache=[0]*len(questions)
        def helper(index):
            if index >= len(questions):
                return 0  
            if cache[index]:
                return cache[index]
        
            points, skip = questions[index]  

   
            included_points = points + helper(index + skip + 1)

      
            not_included_points = helper(index + 1)

            cache[index]=max(included_points, not_included_points)
            return cache[index]
            
        
        return helper(0)




            
