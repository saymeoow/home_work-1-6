#Написать программу в которой нужно будет угадывать число.

#Продумать диапазон чисел (будут жестко заданы или задаваться самим пользователем)
import random

ttry = 0
secret = random.randint(0, 10)

while ttry < 11:
    number = input(f'Введите число: ')
    if number.isdigit():
        number = int(number)
        if number < secret:
            print("Число меньше загаданного!")
        elif number > secret:
            print("Число больше загаданного!")
        else:
            print(f"Вы угадали число - {secret}!")
            break
        ttry += 1
    else:
        print("Введено не число")