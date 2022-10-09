name = input('Напишите свое имя: ')
quit = input()
wrongsim = 0
while wrongsim<1:
    age = int(input(f'Введите возраст: '))
    if age <= 0 and age != int:
        print(f'Ошибка, повторите ввод')
    elif age > 0 and age < 10:
        print(f'''Привет,малыш, {name}''')
    elif age >= 10 and age <= 18:
        print(f'Как дела? {name}')
    elif age > 18 and age <= 120:
        print(f'Что желаете? {name}')
    else:
        print(f'{name},Вы лжете,столько не живут')
        break
        if age == quit:
            break




