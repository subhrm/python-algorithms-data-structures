""" 
Fibonacci Sequence 

F(n) = F(n-1) + F(n-2)
f(0) = 0
f(1) = 1

"""
from time import time

# # UnOPtimized
# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     return fibo(n-1) + fibo(n-2)


def fibo_optimized(n):
    global cache

    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in cache:
        return cache[n]

    res = fibo_optimized(n-1) + fibo_optimized(n-2)
    cache[n] = res
    return res


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    t0 = time()
    res = fibo(n)
    t1 = time()
    print(f"Fibonacci({n}) = {res}")
    print(f"Time: {t1-t0} seconds")
    
    # -- Now try optimized version with just a cache --
    cache ={}
    print("=="*40)
    t0 = time()
    res = fibo_optimized(n)
    t1 = time()
    print(f"Fibonacci({n}) = {res:,}   {n}th power of 2 {2**n:,}")
    print(f"Time: {t1-t0} seconds")



