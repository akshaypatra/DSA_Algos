'''


2054. Two Best Non-Overlapping Events
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

 

Example 1:


Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4
Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.
Example 2:

Example 1 Diagram
Input: events = [[1,3,2],[4,5,2],[1,5,5]]
Output: 5
Explanation: Choose event 2 for a sum of 5.
Example 3:


Input: events = [[1,5,3],[1,5,1],[6,6,5]]
Output: 8
Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.
 

Constraints:

2 <= events.length <= 105
events[i].length == 3
1 <= startTimei <= endTimei <= 109
1 <= valuei <= 106

'''

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        # Sort the events based on their start times.
        events.sort()
        n = len(events)
      
        # 'max_value_after' holds the maximum value of any single event from index i to the end.
        max_value_after = [events[-1][2]] * n
      
        # Fill 'max_value_after' by iterating from the second last to the first event.
        for i in range(n - 2, -1, -1):
            max_value_after[i] = max(max_value_after[i + 1], events[i][2])
      
        # Initialize maximum value to be zero at the start.
        max_value = 0
      
        # Iterate over each event
        for _, end_time, value in events:
            # Find the first event that starts after the current event ends.
            idx = bisect_right(events, end_time, key=lambda x: x[0])
          
            # If such an event is found, add the value of the current event to 
            # the maximum value found after the current event.
            if idx < n:
                combined_value = value + max_value_after[idx]
            else:
                combined_value = value
          
            # Update the maximum value with the larger of the two values.
            max_value = max(max_value, combined_value)
      
        # Return the maximum value found which could be from two or one events.
        return max_value
            
                
                
            


            
            