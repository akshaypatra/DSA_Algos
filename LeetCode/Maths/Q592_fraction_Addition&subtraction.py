# Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

# The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

 

# Example 1:

# Input: expression = "-1/2+1/2"
# Output: "0/1"
# Example 2:

# Input: expression = "-1/2+1/2+1/3"
# Output: "1/3"
# Example 3:

# Input: expression = "1/3-1/2"
# Output: "-1/6"
 

# Constraints:

# The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
# Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
# The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
# The number of given fractions will be in the range [1, 10].
# The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.


# Solution

from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        # My logic 
        # def add_fractions(a, b):
        #     fraction_sum = Fraction(a) + Fraction(b)
        #     return fraction_sum


        # stack=[]
        # i=0
        # while i < len(expression):
        #     number=""
            
        #     if expression[i] in "-+":
        #         number=expression[i:i+4]
        #         i+=4
        #         stack.append(Fraction(int(number[0:2]),int(number[3:])))
        #     if i==0 and (expression[i] in "1234567890"):
        #         number=expression[i:i+3]
        #         i+=3
        #         stack.append(Fraction(int(number[0]),int(number[2:])))
        
        # while stack:
        #     if len(stack)==1:
        #         res=str(stack[0])
        #         if res in "1234567890":
        #             res+="/1"
        #         return res
        #     fraction1=stack.pop()
        #     fraction2=stack.pop()

        #     sum_of_fraction=add_fractions(fraction1, fraction2)
        #     stack.append(sum_of_fraction)

        # Corrected code 
        def add_fractions(a, b):
            return a + b

        stack = []
        i = 0

        while i < len(expression):
            # Find the start of the fraction
            if expression[i] in "+-":
                sign = expression[i]
                i += 1
            else:
                sign = "+"
            
            # Find the numerator
            numerator = ""
            while expression[i].isdigit() or expression[i] == '-':
                numerator += expression[i]
                i += 1
            
            # Skip the slash
            i += 1
            
            # Find the denominator
            denominator = ""
            while i < len(expression) and expression[i].isdigit():
                denominator += expression[i]
                i += 1
            
            # Create the fraction and push to the stack
            fraction = Fraction(int(sign + numerator), int(denominator))
            stack.append(fraction)

        # Add all fractions in the stack
        result = stack.pop()
        while stack:
            result = add_fractions(result, stack.pop())

        # Ensure the result is always returned as a fraction (e.g., "0/1"    instead of "0")
        if result.denominator == 1:
            return f"{result.numerator}/1"   
        else:
            return str(result)
            

# Note : f-string: Introduced in Python 3.6, f-strings are a way to embed expressions inside string literals, using curly braces {}. They are prefixed with the letter f or F. For example, f"{expression}" evaluates the expression and embeds its value in the string. ex:line 108
            


                

        