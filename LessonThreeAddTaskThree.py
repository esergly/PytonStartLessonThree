x = int(input('Введите любое положительное четырёхзначное число: \n'))
one = x // 1000
two = (x // 100) - (one * 10)
three = (x // 10) - ((x // 100) * 10)
four = x % 10

if one + two == three + four:
    print(str(one + two) + ' = ' + str(three + four) + ' - номер "счастливого билета"')
else:
    print(str(one + two) + ' = ' + str(three + four) + ' - повезёт в следующий раз')
