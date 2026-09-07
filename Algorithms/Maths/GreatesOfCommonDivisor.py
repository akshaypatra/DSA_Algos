"""
GREATEST OF COMMON DIVISOR  : The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

"""


def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(7,14)) 
print(gcd(7,15)) 
print(gcd(8,16))
print(gcd(9,14))  