'''

2182. Construct String With Repeat Limit

Medium

You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.
Return the lexicographically largest repeatLimitedString possible.

A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

 

Example 1:

Input: s = "cczazcc", repeatLimit = 3
Output: "zzcccac"
Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.
Example 2:

Input: s = "aababab", repeatLimit = 2
Output: "bbabaa"
Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa". 
The letter 'a' appears at most 2 times in a row.
The letter 'b' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.
 

Constraints:

1 <= repeatLimit <= s.length <= 105
s consists of lowercase English letters.

'''

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Step 1: Count the frequency of each character
        freq = Counter(s)
        
        # Step 2: Create a max heap (-ASCII value ensures lexicographical order)
        max_heap = []
        for char, count in freq.items():
            heapq.heappush(max_heap, (-ord(char), count))
        
        # Step 3: Build the result string
        result = []
        
        while max_heap:
            # Get the largest character
            neg_char, count = heapq.heappop(max_heap)
            char = chr(-neg_char)  # Convert back to character
            
            # How many times can we use this character?
            use_count = min(count, repeatLimit)
            
            # Append the character `use_count` times
            result.append(char * use_count)
            
            # Update the count
            count -= use_count
            
            if count > 0:  # If more of this character remains
                # Check the next largest character
                if not max_heap:
                    break  # No more characters to use, stop the process
                
                # Temporarily use the next largest character
                neg_char2, count2 = heapq.heappop(max_heap)
                char2 = chr(-neg_char2)
                
                # Append one occurrence of the second-largest character
                result.append(char2)
                count2 -= 1  # Update its count
                
                # Push both characters back if there are remaining counts
                if count2 > 0:
                    heapq.heappush(max_heap, (neg_char2, count2))
                heapq.heappush(max_heap, (neg_char, count))
        
        return "".join(result)