'''

3440. Reschedule Meetings for Maximum Free Time II
Solved
Medium

You are given an integer eventTime denoting the duration of an event. You are also given two integer arrays startTime and endTime, each of length n.

These represent the start and end times of n non-overlapping meetings that occur during the event between time t = 0 and time t = eventTime, where the ith meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most one meeting by moving its start time while maintaining the same duration, such that the meetings remain non-overlapping, to maximize the longest continuous period of free time during the event.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event and they should remain non-overlapping.

Note: In this version, it is valid for the relative ordering of the meetings to change after rescheduling one meeting.

 

Example 1:

Input: eventTime = 5, startTime = [1,3], endTime = [2,5]

Output: 2

Explanation:



Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the time [0, 2].

Example 2:

Input: eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]

Output: 7

Explanation:



Reschedule the meeting at [0, 1] to [8, 9], leaving no meetings during the time [0, 7].

Example 3:

Input: eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]

Output: 6

Explanation:



Reschedule the meeting at [3, 4] to [8, 9], leaving no meetings during the time [1, 7].

Example 4:

Input: eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]

Output: 0

Explanation:

There is no time during the event not occupied by meetings.

 

Constraints:

1 <= eventTime <= 109
n == startTime.length == endTime.length
2 <= n <= 105
0 <= startTime[i] < endTime[i] <= eventTime
endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].

'''

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        '''
        -> Note : Order is not preserved
        '''

        n = len(startTime)  # Total number of meetings
        max_free_time = 0  # Variable to hold the maximum free time found
      
        # Calculate the maximum gaps from the left side
        left_gaps = [0] * n
        left_gaps[0] = startTime[0]  # Free time before the first meeting starts
        for i in range(1, n):
            left_gaps[i] = max(left_gaps[i - 1], startTime[i] - endTime[i - 1])
      
        # Calculate the maximum gaps from the right side
        right_gaps = [0] * n
        right_gaps[n - 1] = eventTime - endTime[-1]  # Free time after the last meeting ends
        for i in range(n - 2, -1, -1):
            right_gaps[i] = max(right_gaps[i + 1], startTime[i + 1] - endTime[i])
      
        # Compute the maximum free time by evaluating each meeting
        for i in range(n):
            # Calculate the gap before the current meeting
            left_gap = left_gaps[i] if i == 0 else startTime[i] - endTime[i - 1]
            # Calculate the gap after the current meeting
            right_gap = right_gaps[i] if i == n - 1 else startTime[i + 1] - endTime[i]
          
            # Calculate the total interval of free time
            interval = 0
            if (
                i != 0
                and left_gaps[i - 1] >= (endTime[i] - startTime[i])
                or i != n - 1
                and right_gaps[i + 1] >= (endTime[i] - startTime[i])
            ):
                interval = endTime[i] - startTime[i]
          
            # Update the maximum free time found
            max_free_time = max(max_free_time, left_gap + interval + right_gap)
      
        return max_free_time
