# Recursive Solution

'''
series :  0 1 1 2 3 5 8 ....(n-1)+(n-2)
'''

def fibonacci_series(num):
    if num<=1:
        return num

    return fibonacci_series(num-1)+fibonacci_series(num-2)


n=int(input("Enter index to find the fibonacci number : "))
print(fibonacci_series(n))