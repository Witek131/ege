""""Файл содержит последовательность целых чисел, по модулю не превышающих
10 0 Назовём парой два идущих подряд элемента последовательности.
Определите количество таких пар, в которых запись ровно одного элемента
заканчивается цифрой 7, а сумма квадратов элементов пары меньше, чем квадрат
наименьшего из элементов последовательности, запись которых заканчивается
цифрой 7 В ответе запишите два числа: сначала количество найденных пар,
затем максимальную сумму квадратов элементов этих пар."""
"""a = list(map(int, open('file/17.txt').read().split()))
s1 = 100000000000
for i in a:
    if i < s1 and abs(i) % 10 == 7:
        s1 = i
s1 **= 2
s = 0
d = -111111111111111111
for i in range(len(a) - 1):
    if abs(a[i]) % 10 != 7 and abs(a[i + 1]) % 10 == 7 or abs(a[i]) % 10 == 7 and abs(a[i + 1]) % 10 != 7:
        if a[i] ** 2 + a[i + 1] ** 2<s1:
            s += 1
            if a[i] ** 2 + a[i + 1] ** 2 > d:
                d = a[i]**2 + a[i + 1] ** 2
print(s, d)"""
"""В файле содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от −10000 
до 10000 включительно. Определите и запишите в ответе сначала количество пар элементов последовательности, в которых хотя 
бы одно число делится на 3, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два идущих 
подряд элемента последовательности. Например, для последовательности из пяти элементов: 6; 2; 9; –3; 6— ответ: 4 11.
"""
a = list(map(int, open('file/171.txt').read().split()))
s = 0
s1 = -1000000000000000
for i in range(1, len(a)):
    if a[i] % 3 == 0 or a[i - 1] % 3 == 0:
        s += 1
        if a[i] + a[i - 1] > s1:
            s1 = a[i] + a[i - 1]
print(s, s1)
"""В файле содержится последовательность целых чисел. Элементы последовательности могут принимать целые — значения от -100 000 до 100 000 включительно.
Определите количество троек элементов последовательности, в которых не более двух из трёх элементов содержат в своей записи цифру 3, а сумма элементов тройки не больше максимального элемента последовательности, оканчивающегося на 18.
В ответе запишите количество найденных троек чисел, затем максимальную из сумм элементов таких троек.
В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности."""

f = list(map(int, open('file/17 (2).txt').read().split()))
c = 0
for i in f:
    if i > c and abs(i) % 100 == 18:
        c = i
k = 0
su = []
print(c)
for i in range(len(f) - 2):
    a1 = 0
    a1 = str(f[i]).count('3') > 0
    a1 += str(f[i + 1]).count('3') > 0
    a1 += str(f[i + 2]).count('3') > 0
    if (f[i] + f[i + 1] + f[i + 2] <= c) and a1 <= 2:
        k += 1
        su.append(f[i] + f[i + 1] + f[i + 2])
print(k)
print(max(su))