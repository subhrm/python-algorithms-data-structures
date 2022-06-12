""" 
Fibonacci sequence w/ caching using decorators

F(n) = F(n-1) + F(n-2)
f(0) = 0
f(1) = 1

"""
from functools import lru_cache
from time import time
# from functools import lru_cache

def cache(f):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = f(*args)
        cache[args] = result
        return result

    return wrapper

# @lru_cache
@cache
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibo(n-1) + fibo(n-2)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    t0 = time()
    res = fibo(n)
    t1 = time()
    print(f"Fibonacci({n}) = {res}")
    print(f"Time: {t1-t0} seconds")



