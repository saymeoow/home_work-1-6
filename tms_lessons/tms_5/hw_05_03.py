any_words=('123','121','dwd')

def reverce_func(x):
    if x==x[::-1]:
        return True

res=tuple(filter(reverce_func,any_words))
assert res == ('121','dwd')