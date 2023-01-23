"""Миша заполнял таблицу истинности логической функции
F=¬(y →x) \/ (z →w) \/ ¬z,
но успел заполнить лишь фрагмент из трёх различных её строк, даже не указав, какому столбцу таблицы соответствует каждая из переменных
w, x, y, z.
F
 \0\ \ \0
0\1\ \ \0
1\ \ \0\0
Определите, какому столбцу таблицы соответствует каждая из переменных
w, x, y, z.
В ответе напишите буквыw, x, y, z в том порядке, в котором идут соответствующие им столбцы (сначала буква, соответствующая первому столбцу; затем буква, соответствующая второму столбцу, и т.д.). Буквы
в ответе пишите подряд, никаких разделителей между буквами ставить
не нужно.
"""
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (((not x or y) and (not y or w)) or (z == (x or y))):
#                     pass
#                 else:
#                     print(x, y, z, w)
#                     # yxzw

from itertools import *


def f1(x, y, z, w):
    return not (((not x or y) and (not y or w)) or (z == (x or y)))


s = set()
for a, b, c, d, e, f, g in product([0, 1], repeat=7):
    rows = [[1, a, b, 1],
            [1, c, d, e],
            [f, 1, g, 1]]
    #print(rows)
    for per in permutations('xyzw'):
        if all([f1(**dict(zip(per, row))) == row[-1] for row in rows]):
            s.add(per)
print(s)
