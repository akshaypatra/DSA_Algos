'''
1405. Longest Happy String

Medium

A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0

'''

# Used min heap(priority queue) to store the count and alphabets

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Create a max-heap to store letters with their counts
        heap = []
        
        # Add 'a', 'b', 'c' to the heap with negative counts (since heapq is a min-heap)
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))
        
        result = []
        
        while heap:
            # Pop the character with the highest remaining count
            count1, char1 = heapq.heappop(heap)
            
            # Check if the last two characters are the same as char1
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not heap:
                    break  # No other characters available to avoid "aaa", "bbb", "ccc"
                
                # Use the second most frequent character
                count2, char2 = heapq.heappop(heap)
                result.append(char2)
                count2 += 1  # Decrement the count of char2
                
                # Push char2 back into the heap if there are remaining occurrences
                if count2 < 0:
                    heapq.heappush(heap, (count2, char2))
                
                # Push char1 back into the heap for future use
                heapq.heappush(heap, (count1, char1))
            else:
                # Append char1 to the result
                result.append(char1)
                count1 += 1  # Decrement the count of char1
                
                # Push char1 back into the heap if there are remaining occurrences
                if count1 < 0:
                    heapq.heappush(heap, (count1, char1))
        
        return ''.join(result)
