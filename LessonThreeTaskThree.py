
year = int(input('Введите искомый год: \n'))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('Введённый год является високосным. В нём 366 дней.')
else:
    print('Введённый год не является високосным. В нём 365 дней.')
