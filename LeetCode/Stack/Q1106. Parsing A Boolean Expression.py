'''
1106. Parsing A Boolean Expression

Hard

A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.

 

Example 1:

Input: expression = "&(|(f))"
Output: false
Explanation: 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.
Example 2:

Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.
Example 3:

Input: expression = "!(&(f,t))"
Output: true
Explanation: 
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.
 

Constraints:

1 <= expression.length <= 2 * 104
expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.

'''




class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for char in expression:
            if char == ')':
                # Gather all the operands for the current subexpression
                operands = []
                while stack[-1] != '(':
                    operands.append(stack.pop())
                stack.pop()  # pop '('
                
                operator = stack.pop()
                if operator == '!':
                    # NOT operation, invert a single operand
                    result = not (operands.pop() == 't')
                elif operator == '&':
                    # AND operation, all operands must be True
                    result = all(op == 't' for op in operands)
                elif operator == '|':
                    # OR operation, at least one operand must be True
                    result = any(op == 't' for op in operands)
                
                # Push the result back to stack as 't' or 'f'
                stack.append('t' if result else 'f')
            
            elif char != ',':
                # Push everything except ',' into the stack
                stack.append(char)
        
        # Final result will be in stack
        return stack[0] == 't'