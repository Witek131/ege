"""Миша заполнял таблицу истинности логической функции
F=¬(y →x) \/ (z →w) \/ ¬z,
но успел заполнить лишь фрагмент из трёх различных её строк, даже не указав, какому столбцу таблицы соответствует каждая из переменных
w, x, y, z.
F
 \0\ \0
0\1\ \0
1\ \0\0
Определите, какому столбцу таблицы соответствует каждая из переменных
w, x, y, z.
В ответе напишите буквыw, x, y, z в том порядке, в котором идут соответствующие им столбцы (сначала буква, соответствующая первому столбцу; затем буква, соответствующая второму столбцу, и т.д.). Буквы
в ответе пишите подряд, никаких разделителей между буквами ставить
не нужно.
"""
from itertools import *

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (not y or x) or (not z or w) or not z:
                    pass
                else:
                    print(x, y, z, w)
                    # yxzw


def r(x, y, z, w):
    return not(not (not y or x) or (not z or w) or not z)


for a, b, c, d in product([0, 1], repeat=4):
    t = ((a, 0, b, 0, 1),
         (0, 1, c, 0, 1),
         (1, d, 0, 0, 1))
    if len(set(t)) == len(t):
        for i in permutations('xyzw'):
            if all(r(**dict(zip(i, j))) == 0 for j in t):
                print(*i)
