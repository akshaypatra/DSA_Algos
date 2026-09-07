'''
20. Valid Parentheses
Solved
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''

class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Using Hashmap and stack
        '''

        h = {
            '{': '}',
            '[': ']',
            '(': ')'
        }

        stack = []

        for ch in s:
            if ch in h:  # opening bracket
                stack.append(ch)
            else:  # closing bracket
                if not stack:
                    return False

                top = stack.pop()

                if h[top] != ch:
                    return False

        return len(stack) == 0


        

        '''
        using set , beats 100%

        '''

        stk = []
        s1 = set("({[")
        for i in s:
            if i in s1:
                stk.append(i)
                continue
            if not stk: return False
            if i == ")" and stk[-1] == "(":
                stk.pop()
            elif i == "]" and stk[-1] == "[":
                stk.pop()
            elif i == "}" and stk[-1] == "{":
                stk.pop()
            else:
                return False
        if not stk:
            return True
        return False