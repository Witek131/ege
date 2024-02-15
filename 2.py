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

def f(x, y, z, w):
    # выражение из задания
    return y and (x <= w) and ((not x) <= (w != z))


for a, b, c, d, e in product([0, 1], repeat=5):
    rows = [(0, 0, a, b), (0, c, d, 0), (1, 1, 1, e)]
    valu = [1, 1, 0]
    if len(set(rows)) != len(rows):
        continue
    for perm in permutations('xyzw'):
        if all([f(**dict(zip(perm, row))) == val
                for row, val in zip(rows, valu)]):
            print(perm)

'''
def f(x, y, z, w):
    return (z <= w) and y and not x


from itertools import *

# таблица из задания
# на месте пропусков 2
table = [[0, 1, 2, 0, 1],
         [2, 0, 2, 2, 1],
         [0, 1, 1, 2, 0]]
# все значения для 4 переменных
rows = list(product([0, 1], repeat=4))
# перебираем все перестановки столбцов
for order in permutations('xywz'):
    # перебираем все возможные комбинации из строк
    for check in permutations(rows, r=len(table)):
        # если все строки из таблицы соответствуют
        # соответствуют выбранным строкам
        # и значению функции для них
        if all(a in (2, b) for t_row, row in zip(table, check) for a, b in
               zip(t_row, (*row, f(**dict(zip(order, row)))))):
            # выводим найденную перестановку
            print(*order, sep='')
            break
'''