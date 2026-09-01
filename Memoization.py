# def count_keys(d):
#     count = 0
#     for key, value in d.items():
#         count += 1
#         if isinstance(value, dict):
#             count += count_keys(value)
#     return count

# config = {
#     "database": {
#         "host": "localhost",
#         "port": 5432,
#         "credentials": {
#             "user": "admin",
#             "password": "secret"
#         }
#     },
#     "debug": True
# }

# print(count_keys(config))   # 7

# naive recursion
# def fib_recursion(n):
#     if n <=1:
#         return n
#     return fib_recursion(n-1)+fib_recursion(n-2)
# print(fib_recursion(10))

# # 2. Iterative Fibonacci

# def fib_iterative(n):
#     if n<=1:
#         return n
#     a,b=0,1
#     for i in range(2,n+1):
#         a,b=b,a+b
#     return b
# print(fib_iterative(10))


from functools import lru_cache
@lru_cache(maxsize=None)
def fib_cache(n):
    if n<=1:
        return n
    return fib_cache(n-1)+fib_cache(n-2)
print(fib_cache(10))

from functools import lru_cache

# Counters
recursive_calls = 0
iterative_calls = 0
cached_calls = 0


# 1. Naive recursive
def fib_recursive(n):
    global recursive_calls
    recursive_calls += 1

    if n <= 1:
        return n

    return fib_recursive(n - 1) + fib_recursive(n - 2)


# 2. Iterative
def fib_iterative(n):
    global iterative_calls
    iterative_calls += 1

    if n <= 1:
        return n

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


# 3. Recursive with caching
@lru_cache(maxsize=None)
def fib_cached(n):
    global cached_calls
    cached_calls += 1

    if n <= 1:
        return n

    return fib_cached(n - 1) + fib_cached(n - 2)


# Test with n = 30
n = 30

print("fib_recursive(30) =", fib_recursive(n))
print("Function calls    =", recursive_calls)

print()

print("fib_iterative(30) =", fib_iterative(n))
print("Function calls    =", iterative_calls)

print()

print("fib_cached(30)    =", fib_cached(n))
print("Function calls    =", cached_calls)