from datetime import datetime

def square_func(func):
    def wrap(time):
        square = [i**2 for i in range(1, 5)]
        print(square)
        res=func(time)
        return res

    return wrap

@square_func
def time_func(time):
    return f'{time}'


res=time_func(datetime.now())
print(res)