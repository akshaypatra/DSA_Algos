'''
1353. Maximum Number of Events That Can Be Attended
Solved
Medium

You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startDayi <= d <= endDayi. You can only attend one event at any time d.

Return the maximum number of events you can attend.


Example 1:


Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
 

Constraints:

1 <= events.length <= 105
events[i].length == 2
1 <= startDayi <= endDayi <= 105

'''

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        '''
        Missing point in description : 
            The event only takes 1 day and it can be attended between [start day, end date]
            for example : if [startDay,endDay]=[1,3] -> so event can be attened at either day 1 , day 2 , or day 3


        Algorithm :

        1. sort the events according to start date
        2. find the event whose start data <= given date
        3. select event with lowest end data on that given day
        4. Eliminate all end dates < day (from the pq)

        Data structure to use : Prority queue (to give priority to lowest end date) - heapq in python 

        '''
        import heapq

        events.sort()
        l = len(events)
        index = 0
        day = 0
        result = 0

        pq = []  # priority queue to mainatin lowest end day (on a given day)

        while len(pq)!=0 or index < l :
            if len(pq)==0 :
                day = events[index][0]
            
            while index < l and events[index][0]<= day :
                heapq.heappush(pq,events[index][1]) # add the end date to pq (to trach lowest end date)
                index+=1

            heapq.heappop(pq)
            day+=1
            result+=1

            #  flush all ends <=  day form pq
            while len(pq)!=0 and pq[0]<day:
                heapq.heappop(pq)
            
        return result
                


        

        




        
