first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second == third:
    print('Количество совпадений = 3')
elif first == second:
    print('Количество совпадений = 2')
elif first == third:
    print('Количество совпадений = 2')
elif second == third:
    print('Количество совпадений = 2')
else:
    print('Количество совпадений = 0')

# Условная конструкция. Операторы if, elif, else. Д/з сдано 2024/06/11 09:30
