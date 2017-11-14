# Задача 1

print('Введите четыре числа для сравнения.')
one = int(input("Первое число \n"))
two = int(input("Второе число \n"))
three = int(input("Третье число \n"))
four = int(input("Четвёртое число \n"))

if one >= two and one >= three and one >= four:
    print('Максимальное из введённых число ' + str(one))
elif two >= one and two >= three and two >= four:
    print('Максимальное из введённых число ' + str(two))
elif three >= one and three >= two and three >= four:
    print('Максимальное из введённых число ' + str(three))
elif four >= one and four >= two and four >= three:
    print('Максимальное из введённых число ' + str(four))
