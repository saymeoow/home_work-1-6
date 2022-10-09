numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def search(n):
    if n % 3 == 0:
        return True
    elif n % 5 == 0:
        return True


res=sum(list(filter(search,numbers)))
assert res==60


