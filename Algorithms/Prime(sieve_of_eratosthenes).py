'''
The Sieve of Eratosthenes is an efficient algorithm for finding all prime numbers up to a given integer n.
.It works by iteratively marking the multiples of each prime starting from 2.

Algorithm Steps:
1. Create a boolean array is_prime of size n+1 and initialize all values to True.
2. Set is_prime[0] and is_prime[1] to False since 0 and 1 are not prime.
3. Start from the first prime number (2) and mark all its multiples as False.
4. Move to the next unmarked number (which is prime) and mark all its multiples.
5. Repeat this process up to sqrt(n) , as all non-prime numbers will have been marked by this point.
6. The remaining True indices in the array represent prime numbers.

'''

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime

    for i in range(2, int(n**0.5) + 1):  # Iterate up to sqrt(n)
        if is_prime[i]:  # If i is prime
            for j in range(i * i, n + 1, i):  # Mark multiples of i
                is_prime[j] = False

    return [i for i in range(n + 1) if is_prime[i]]  # Return all prime numbers

# Example usage:
print(sieve_of_eratosthenes(50))

