'''
Leetcode 539 : Minimum Time Difference

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 
Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0


'''

# SOLUTION 

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def subtract_time(a,b):
            hr_a = int(a[:2])
            min_a = int(a[3:])
            hr_b = int(b[:2])
            min_b = int(b[3:])
            
            # Convert times to minutes since midnight
            total_a = hr_a * 60 + min_a
            total_b = hr_b * 60 + min_b
            
            # Direct difference
            diff = abs(total_b - total_a)
            
            # Circular difference (crossing midnight)
            circular_diff = 1440 - diff  # 1440 is the total number of minutes in 24 hours
            
            return min(diff, circular_diff)

        timePoints.sort()
        current_min=subtract_time(timePoints[0],timePoints[len(timePoints)-1])
        i=0
        j=1
        while j<len(timePoints):
            current_min=min(current_min, subtract_time(timePoints[i],timePoints[j]))
            i+=1
            j+=1
        return current_min 
        




        