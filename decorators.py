import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        time_took=end-start
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper    

def retry(n):
    def decorator_fun(fun):
        def wrapper(*args,**kwargs):
            for i in range(n):
                try:
                    return fun(*args,**kwargs)
                except Exception as e:
                    print(f'Retrying... attempt {i+1}/{n}. Error: {e}')
            raise Exception("All retries failed")        
        return wrapper
    return decorator_fun    


def memoize(func):
    cache={}
    def wrapper(*args):
        
        if args in cache:
            return cache[*args]
        result = func(*args)
        cache[args] = result
        return result    
        
    return wrapper           

def validate_types(func):
    def wrapper(*args, **kwargs):
        hints = func.__annotations__
        params = list(hints.keys())
        for i, arg in enumerate(args):
            if i < len(params) and params[i] != 'return':
                expected = hints[params[i]]
                if not isinstance(arg, expected):
                    raise TypeError(f"Argument {params[i]} must be {expected.__name__}")
        return func(*args, **kwargs)
    return wrapper

@timer
def slow(n):
    time.sleep(n)
    return "done"

@retry(3)
def might_fail():
    import random
    if random.random() < 0.7:
        raise ValueError("failed")
    return "success"

@memoize
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

@validate_types
def add(x: int, y: int) -> int:
    return x + y

print(slow(1))
print(might_fail())
print(fib(10))
print(add(1, 2))
print(add("a", 2))  # should raise TypeError

