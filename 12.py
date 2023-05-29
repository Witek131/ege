"""Дана программа для Редактора:
НАЧАЛО
ПОКА нашлось (>1) ИЛИ нашлось (>2) ИЛИ нашлось (>0)
 ЕСЛИ нашлось (>1)
 ТО заменить (>1, 22>)
 КОНЕЦ ЕСЛИ
 ЕСЛИ нашлось (>2)
 ТО заменить (>2, 2>)
 КОНЕЦ ЕСЛИ
 ЕСЛИ нашлось (>0)
 ТО заменить (>0, 1>)
 КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
12
Демонстрационный вариант ЕГЭ 2023 г. ИНФОРМАТИКА, 11 класс. 13 / 22
© 2023 Федеральная служба по надзору в сфере образования и науки
На вход приведённой выше программе поступает строка, начинающаяся
с символа «>», а затем содержащая 39 цифр «0», n цифр «1» и 39 цифр «2»,
расположенных в произвольном порядке.
Определите наименьшее значение n, при котором сумма числовых значений
цифр строки, получившейся в результате выполнения программы, является
простым числом. """


def prost(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(1, 500):
    s = '>' + '0' * 39 + '1' * i + '2' * 39
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    n = 0
    for j in s:
        if j != '>':
            n += int(j)
    if prost(n):
        print(i, n)
        break
'''Какое количество вариантов строки можно получить в результате работы приведенного ниже алгоритма, 
если использовать четыре 1, три 3 и две 2 на входе?
НАЧАЛО
ПОКА нашлось (133) ИЛИ нашлось (221) ИЛИ нашлось (23) ЕСЛИ нашлось (133)
ТО заменить (133, 1)
ЕСЛИ нашлось (221)
ТО заменить (221,31)
ЕСЛИ нашлось (23)
ТО заменить (23, 21)
КОНЕЦ ПОКА 
КОНЕЦ
'''
from itertools import permutations

ss = [''.join(s) for s in permutations('1' * 4 + '3' * 3 + '2' * 2)]
#print(ss)
d=[]
for s in ss:
    while '133' in s or '221' in s or '23' in s:
        s = s.replace('133', '1', 1)
        s = s.replace('221', '31', 1)
        s = s.replace('23', '21', 1)
    d.append(s)
print(len(set(d)))
