'''
3169. Count Days Without Meetings
Solved
Medium

You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.

 

Example 1:

Input: days = 10, meetings = [[5,7],[1,3],[9,10]]

Output: 2

Explanation:

There is no meeting scheduled on the 4th and 8th days.

Example 2:

Input: days = 5, meetings = [[2,4],[1,3]]

Output: 1

Explanation:

There is no meeting scheduled on the 5th day.

Example 3:

Input: days = 6, meetings = [[1,6]]

Output: 0

Explanation:

Meetings are scheduled for all working days.

 

Constraints:

1 <= days <= 109
1 <= meetings.length <= 105
meetings[i].length == 2
1 <= meetings[i][0] <= meetings[i][1] <= days

'''

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # Sort meetings by start time
        merged = []
        
        for start, end in meetings:
            if merged and merged[-1][1] >= start:
                merged[-1][1] = max(merged[-1][1], end)  # Merge overlapping intervals
            else:
                merged.append([start, end])

        free_days = merged[0][0] - 1  # Days before the first meeting
        last_meeting_end = merged[0][1]

        for i in range(1, len(merged)):
            free_days += merged[i][0] - last_meeting_end - 1  # Count free days between meetings
            last_meeting_end = merged[i][1]

        free_days += days - last_meeting_end  # Days after the last meeting
        return free_days


            
            

