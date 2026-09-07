'''
Memoization Solution 

step 1 : initialize the DP array of size (n+1) to store the values of each recursive call;
step 2 : store the value of f(n) in DP[n]
step 3 : check if the subproblem is already solved or not 
step 4 : if yes , return the stored value

TC : O(n)
SC : O(n)


'''





n=int(input("Enter the index to find the fibonacci number : "))

DP=[-1]*(n+1)


def fib_series(n):

    if n<=1:
        DP[n]=n
        return n
    
    if DP[n]!=-1:
        return DP[n]

    DP[n]=fib_series(n-1)+fib_series(n-2)
    return DP[n]


print(fib_series(n))

    
