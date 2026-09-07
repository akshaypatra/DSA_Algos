def prime_factors(n):
    factors = []
    # Start by dividing the number by 2 to remove all even factors
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Now the number must be odd, so we start with 3 and go up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    # If n is a prime number greater than 2, it will be left at the end
    if n > 2:
        factors.append(n)
    
    return set(factors)

# Example usage
number = 56
print("Prime factors of", number, "are:", prime_factors(number))