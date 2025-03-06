from functools import lru_cache

def cache(func):
    cache_dict = {}
    
    def wrapper(*args):
        print(cache_dict)
        if args not in cache_dict:
            cache_dict[args] = func(*args)
        return cache_dict[args]
    return wrapper

def fib():
    a, b = 0, 1
    
    @cache
    def next_fib(n):
        nonlocal a, b
        if n == 0:
            return a
        s = a
        a, b = b, a + b
        return s
    
    counter = 0
    
    def wrapper():
        nonlocal counter
        result = next_fib(counter)
        counter += 1
        return result
    
    return wrapper

fibonacci = fib()
for _ in range(10):
    print(fibonacci())


# def fib():
#     a, b = 0, 1
#     def next_fib():
#         nonlocal a, b
#         a, b = b, a + b
#         return a
#     return next_fib
# s = fib()
# for _ in range(10):
#     print(s())



