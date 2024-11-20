'''

2516. Take K of Each Character From Left and Right

Medium

You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

 

Example 1:

Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.
Example 2:

Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.

'''

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        char_count = Counter(s)
      
        
        if any(char_count[char] < k for char in "abc"):
            return -1  
      
        
        max_length = start_index = 0
      
        
        for i, c in enumerate(s):
            char_count[c] -= 1  
            while char_count[c] < k:
                char_count[s[start_index]] += 1  # Increment the character at start index
                start_index += 1  # Move the start index forward
          

            max_length = max(max_length, i - start_index + 1)
      
       
        return len(s) - max_length