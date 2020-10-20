n = int(input())

def in_cache(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]
    return wrapper

@in_cache
def factorial_recursive(n):
    return n * factorial_recursive(n-1) if n > 1 else 1

fac = factorial_recursive(n)

print(fac//(n*(n//2)))