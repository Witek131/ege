"""Дана последовательность натуральных чисел. Необходимо определить
количество её непрерывных подпоследовательностей, сумма элементов
которых кратна 999.
Входные данные
Первая строка входного файла содержит целое число N – общее количество
чисел в наборе. Каждая из следующих N строк содержит одно число.
Гарантируется, что общая сумма всех чисел и число в ответе не превышают
2 ∙ 109.
Вам даны два входных файла (A и B), каждый из которых имеет"""

s = list(map(int, open("file/27-B.txt").read().split()[1:]))
f = 0
ss = 0
d = [0] * 999
d[0] = 1
for i in range(len(s)):
    f += s[i]
    ss += d[f % 999]
    d[f % 999] += 1
print(ss)

'''Дана последовательность натуральных чисел. Назовём парой любые два
числа из последовательности. Необходимо определить количество пар,
в которых сумма чисел в паре делится без остатка на 3, а их произведение –
на 4096.
Входные данные
Первая строка входного файла содержит целое число N – общее количество
чисел в наборе. Каждая из следующих N строк содержит одно число,
не превышающее 40 000. Гарантируется, что число в ответе не превышает
2 ∙ 109
.
Вам даны два входных файла (A и B), каждый из которых имеет описанную
выше структуру. В ответе укажите два числа: сначала искомое значение для
файла A, затем – для файла B.'''


def f(n):
    count = 0
    while not n % 2:
        count += 1
        n //= 2
    if count > 10:
        count = 10
    return count


f = open('file/27-A1.txt')
f=[int(i) for i in f][1:]
pri

