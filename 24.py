"""Текстовый файл содержит только буквы A, C, D, F, O. Определите длину самой
длинной цепочки символов, которая начинается и заканчивается буквой F,
а между двумя последовательными буквами F содержит не более двух букв A
и произвольное количество других букв.

 """
f = open('file/24.txt').read()
f = f.split('F')
s = -1
for i in f:
    if i.count('A') <= 2 and len(i) > s:
        s = len(i)
        d = f.index(i)
if d != 0 or d != len(f) - 1:
    print(s + 2)
else:
    print(s + 1)
"""Текстовый файл содержит строку из заглавных латинских букв X, Y и Z. Определите максимальное
количество идущих подряд троек символов ZXY или ZYX.
Ссылка на файл"""

s = open('file/3021.txt').readline()
mx = c = 0
for st in range(3):
    for i in range(st, len(s), 3):
        if s[i:i + 3] in ('ZXY', 'ZYX'):
            c += 1
        else:
            c = 0
        mx = max(mx, c)
print(mx)
"""Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите максимальное количество идущих 
подряд символов, среди которых каждые два соседних различны.
Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать 
с помощью данного алгоритма.
"""
s = open('file/24inf.txt').read().split()
mx = 0
c = 1
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        c += 1
        if c > mx:
            mx = c
    else:
        c = 1

print(mx)


"""Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. 
Строки содержат только заглавные буквы латинского алфавита (ABC…Z). Определите количество строк, в 
которых буква E встречается чаще, чем буква A.
Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо 
обработать с помощью данного алгоритма."""