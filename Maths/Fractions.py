from fractions import Fraction


# fraction add function
def add_fractions(a, b):
    fraction_sum = Fraction(a) + Fraction(b)
    return fraction_sum


fraction1 = Fraction(-4, 1)  # 1/3
fraction2 = Fraction(6, 1)  # 1/6

result = add_fractions(fraction1, fraction2)
print("The sum of the fractions is:", result)

# to access the numerator : fraction1.numerator
print(fraction1.numerator)

# to access the denominator : fraction1.dinomerator
print(fraction1.denominator)

# to get sum directly
print(fraction1+fraction2)
