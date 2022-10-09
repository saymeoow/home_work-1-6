stroka=input(f'Введите значение: ')

def func(n):
    if n.isdigit():
        n=float(n)
        if n < 0:
            print(f'Вы ввели отрицательне число {stroka}')
        elif n >= 0:
            print(f'Вы ввели положительне число число {stroka}')
        elif n==float:
            print(f'Вы ввели дробное число {stroka}')
        return True


res=list(filter(func,stroka))
print(res)
