from functools import lru_cache




@lru_cache
def fib( n: int) -> int:
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)

# Notes

# The @lru_cache is a decorator in Python's functools module that implements a simple caching mechanism, known as "Least Recently Used" (LRU) caching. It can be used to optimize the performance of functions by storing the results of expensive function calls and returning the cached result when the same inputs occur again.

# How @lru_cache Works
# Caching: When you decorate a function with @lru_cache, it automatically caches the results of the function for each set of arguments it has seen before. If the function is called again with the same arguments, the cached result is returned instead of recalculating the result.
# LRU Mechanism: The cache has a maximum size (which can be specified), and when it is full, the least recently used items are discarded to make room for new ones. This ensures that the cache remains efficient in terms of memory usage.