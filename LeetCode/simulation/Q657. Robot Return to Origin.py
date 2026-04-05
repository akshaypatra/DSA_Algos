'''
657. Robot Return to Origin
Solved
Easy

There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

 

Example 1:

Input: moves = "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
Example 2:

Input: moves = "LL"
Output: false
Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.
 

Constraints:

1 <= moves.length <= 2 * 104
moves only contains the characters 'U', 'D', 'L' and 'R'.
'''

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        '''

        Approach 1 : Bruteforce + hashmap
            - adding the directions magnitude to cur_position
            - checking if cur==[0,0]
        
             (0,1)
        (1,0)(1,1)(1,2)
             (2,1)

        SC : O(1)
        TC : O(n)
       
        '''
        # direction={
        #     'U':(-1,0),
        #     'D':(1,0),
        #     'R':(0,1),
        #     'L':(0,-1)
        # }


        # cur=[0,0]
        # for i in moves :
        #     cur[0]+=direction[i][0]
        #     cur[1]+=direction[i][1]
        
        # return cur==[0,0]


        '''
        Aproach 2 : Simulation (without hashmap)
        '''

        # x = y = 0
        # for move in moves:
        #     if move == 'U': y -= 1
        #     elif move == 'D': y += 1
        #     elif move == 'L': x -= 1
        #     elif move == 'R': x += 1

        # return x == y == 0

        '''
        Optimized approach : (Counting the positions)
            if count of all positions moved is equal then the robot returned to same place.

            count(right) == count(left)
            and 
            count(down) == count (up)

        '''

        return moves.count('U')==moves.count('D') and moves.count('L')==moves.count('R')
