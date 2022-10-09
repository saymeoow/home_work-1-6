#Написать программу, которая получает имя и возраст пользователя, проверяет возраст и выдает приветственное сообщениев зависимости от возраста:
name = input('Напишите свое имя: ')
wrongsim = 0
while wrongsim<1:
    age = int(input(f'Введите возраст: '))
    if age <= 0 and age != int:
        print(f'Ошибка, повторите ввод')
    elif age > 0 and age < 10:
        print(f'''Привет,малыш, {name}''')
        break
    elif age >= 10 and age <= 18:
        print(f'Как дела? {name}')
        break
    elif age > 18 and age <= 120:
        print(f'Что желаете? {name}')
        break
    else:
        print(f'{name},Вы лжете,столько не живут')
        break