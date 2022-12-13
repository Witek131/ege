"""Операнды арифметического выражения записаны в системах счисления с основаниями 9 и 11:

88x4y9 + 7x44y11

В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры. Определите значения x и y, при которых значение данного арифметического выражения будет наименьшим и кратно 61. Для найденных значений x и y вычислите частное от деления значения арифметического выражения на 61 и укажите его в ответе в десятичной системе счисления. Основание системы счисления в ответе указывать не нужно."""

for x in range(9):
    for y in range(9):
        a = str(x)
        b = str(y)
        if (int('88' + a + '4' + b, 9) + int('7' + a + '44' + b, 11)) % 61 == 0:
            print(x, y, (int('88' + a + '4' + b, 9) + int('7' + a + '44' + b, 11)) // 61)