def lazy_range(start, stop, step=1):
    current = start
    while current < stop:
        yield current       # give current value, pause
        current += step     # when resumed, move to next

def lazy_map(func, iterable):
    for i in iterable:
        yield func(i)


def lazy_filter(pred, iterable):
    for i in iterable:
        if pred(i):
            yield i

    
def lazy_take(n, iterable):
    count = 0
    for item in iterable:
        if count >= n:
            break
        yield item
        count += 1

squares = lazy_map(lambda x: x**2, lazy_range(1, 1001))
even_squares = lazy_filter(lambda x: x % 2 == 0, squares)
result = list(lazy_take(5, even_squares))
print(result)   