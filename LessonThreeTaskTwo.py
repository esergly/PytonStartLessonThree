

num = int(input('Введите номер искомой квартиры: \n'))

if num > (4 * 9 * 4) or num < 1:
    print('Такой квартиры в этом доме нет.')
else:
    podiezd = (num // 36) + 1
    etazh = 9 - ((podiezd * 36 - num) // 4)
    print('Квартира расположена на ' + str(etazh) + ' этаже подъезда ' + str(podiezd))
