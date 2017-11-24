x = int(input('Введите любое положительное шестизначное число: \n'))

one = x // 100000
two = (x // 10000) - (one * 10)
three = (x // 1000) - ((one * 100) + (two * 10))
four = (x // 100) - ((one * 1000) + (two * 100) + (three * 10))
five = (x // 10) - ((one * 10000) + (two * 1000) + (three * 100) + (four * 10))
six = x % 10

if one == six and two == five and three == four:
    print(str(x) + ' - число является палиндром')
else:
    print(str(x) + ' - число не является палиндром')
