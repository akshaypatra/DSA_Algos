'''
Tabulation technique 

-> bottom - up approach


step 1 : initialise the DP array of size n+1
step 2 : insert values of base cases in DP array
step 3 : calculate the required answer using the base cases 

TC : O(n)
SC : O(n)

'''


def fib_series(n):

    if n<=1:
        return n
    
    DP=[-1]*(n+1)

    # Base cases
    DP[0]=0
    DP[1]=1

    # Looping
    for i in range(2,n+1):
        DP[i]=DP[i-1]+DP[i-2]
    
    return DP[n]


# n=int(input("Enter the index of fibonacci number : "))
# print(fib_series(n))
    

# Space Optimized Solution using Two pointers  , SC : O(1)
 
def fib_series_optimized(n):
    if n<=1:
        return n
    
    p1=0
    p2=1
    
    for i in range(2,n+1):
        cur=p1+p2

        p1=p2
        p2=cur
    
    return p2

n=int(input("Enter the index of fibonacci number : "))
print(fib_series_optimized(n))