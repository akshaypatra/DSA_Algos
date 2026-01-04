# Function to find all divisors of a given number n
# Time Complexity: O(√n)
# Space Complexity: O(k) where k is the number of divisors



def get_divisors(n):

        divisors = []
        limit = n ** 0.5
        i = 1
        while(i <= limit):

            if(n % i == 0):
                divisors.append(i)
                
                poss_div = n//i # potential divisor 
                if(poss_div != i):
                    divisors.append(poss_div)

            i += 1
        
        return divisors
print(get_divisors(21))
