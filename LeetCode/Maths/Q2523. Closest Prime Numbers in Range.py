'''

2523. Closest Prime Numbers in Range
Solved
Medium

Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.


'''


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Initialize a counter for primes
        prime_count = 0
      
        # Initialize a list to mark non-prime numbers
        sieve = [False] * (right + 1)
      
        # Initialize a list to store prime numbers
        primes = [0] * (right + 1)
      
        # Populate the sieve and primes list using the Sieve of Eratosthenes
        for i in range(2, right + 1):
            if not sieve[i]:
                primes[prime_count] = i
                prime_count += 1
            j = 0
            while primes[j] <= right // i:
                sieve[primes[j] * i] = True
                if i % primes[j] == 0:
                    break
                j += 1
      
        # Filter primes within the given range [left, right]
        filtered_primes = [v for v in primes[:prime_count] if left <= v <= right]
      
        # Initialize minimum difference as infinity
        min_difference = inf
      
        # Initialize answer with a pair of -1 to indicate no primes found
        closest_pair = [-1, -1]
      
        # Iterate over each pair of subsequent primes to find the closest pair
        for a, b in zip(filtered_primes, filtered_primes[1:]):
            difference = b - a
            if difference < min_difference:
                min_difference = difference
                closest_pair = [a, b]
      
        # Return the closest pair of prime numbers
        return closest_pair
            
