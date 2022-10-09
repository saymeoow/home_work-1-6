def memo_func(f):
    cache = dict()

    def save_cache_func(*args):
        print(f"run from cache={args}")
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return save_cache_func


@memo_func
def multi_func(a,b):
    print(f'run without cache({a},{b})')
    return a*b

print(multi_func(2,3),'\n')
print(multi_func(2,3),'\n')
print(multi_func(3,5),'\n')
print(multi_func(3,5),'\n')
