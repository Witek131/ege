f = open('file/9.csv').read().split('\n')[1:-6]
l = 0
s1 = 0
m = - 100000000
for i in f:
    i = i.replace(',', '.')
    s = list(map(float, i.split(';')[1:]))
    l += len(s)
    if m < max(s):
        m = max(s)
    s1 += sum(s)
print(m - (s1 / l))
"""В каждой строке электронной таблицы записаны четыре натуральных числа. 
Определите, сколько в таблице таких четвёрок, из которых можно выбрать 
три числа, которые не могут быть сторонами никакого треугольника, в том 
числе вырожденного (вырожденным называется треугольник, у которого 
сумма длин двух сторон равна длине третьей стороны). 08022022
"""
f = open('file/09.csv').read().split('\n')[:-1]
s = 0
for i in f:
    a = list(map(int, i.split(';')))
    a.sort()
    if sum(a[:2]) < a[3]:
        s += 1
print(s)
