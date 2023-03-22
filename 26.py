"""На складе хранятся кубические контейнеры двух цветов различного размера.
Чтобы сократить занимаемое при хранении место, контейнеры вкладывают
друг в друга. Чтобы вложенные контейнеры было лучше видно, их цвета при
вложении обязательно должны чередоваться, то есть нельзя вкладывать
контейнер в контейнер такого же цвета. Один контейнер можно вложить
в другой, если размер стороны внешнего контейнера превышает размер
стороны внутреннего на 7 и более условных единиц. Группу вложенных друг
в друга контейнеров называют блоком. Количество контейнеров в блоке
может быть любым. Каждый блок, независимо от количества и размера
входящих в него контейнеров, а также каждый одиночный контейнер, не
входящий в блоки, занимает при хранении одну складскую ячейку.
Зная размеры и цвета всех контейнеров, определите максимально возможное
количество контейнеров в одном блоке и минимальное количество ячеек для
хранения всех контейнеров.
Входные данные
Каждая строка входного файла содержит натуральное число и букву A или B.
Число обозначает размер контейнера в условных единицах, буква – цвет
этого контейнера (буквами A и B условно обозначены два цвета).
В ответе запишите два целых числа: сначала максимально возможное
количество контейнеров в одном блоке, затем минимальное количество ячеек
для хранения всех контейнеров. """
f = open('file/26.txt').read().split('\n')
s = []
for i in f:
    s1 = i.split()
    if s1:
        s.append([int(s1[0]), s1[1], 0])
k = 0
s.sort()
n = 0
j = 0
while n < len(s):
    a = 0

    for i in range(j, len(s)):
        if s[i][2] == 0:
            k += 1
            s[i][2] = 1
            saa = s[i][1]
            j = i
            n += 1
            sqq = s[i][0]
            break

    for i in range(j+1, len(s)):
        # print(s[i][1] != saa , s[i][2] == 0 , s[i][0] + 7 <= sqq)
        if s[i][1] != saa and s[i][2] == 0 and s[i][0] - 7 >= sqq:
            s[i][2] = 1
            saa = s[i][1]
            n += 1
            sqq = s[i][0]
print(s)
print(k)
"""На складе хранятся кубические контейнеры различного размера. Чтобы 
сократить занимаемое при хранении место, контейнеры вкладывают друг 
в друга. Один контейнер можно вложить в другой, если размер стороны 
внешнего контейнера превышает размер стороны внутреннего на 5 и более 
условных единиц. Группу вложенных друг в друга контейнеров называют 
блоком. Количество контейнеров в блоке может быть любым. Каждый блок, 
независимо от количества и размера входящих в него контейнеров, а также 
каждый одиночный контейнер, не входящий в блоки, занимает при хранении 
одну складскую ячейку. 
Зная количество контейнеров и их размеры, определите минимальное 
количество ячеек для хранения всех контейнеров и максимально возможное 
количество контейнеров в одном блоке. 
Входные данные 
Первая строка входного файла содержит целое число N – общее количество 
контейнеров. Каждая из следующих N строк содержит натуральное число, 
не превышающее 10 000, – размер контейнера в условных единицах. 
В ответе запишите два целых числа: сначала минимальное количество ячеек 
для хранения всех контейнеров, затем максимально возможное количество 
контейнеров в одном блоке. """


f = list(map(int, open('file/26(1).txt').read().split()))[1:]

f.sort(reverse=True)
s = 0
g = [0] * 10000
n = 0
for i in range(len(f) - 1):
    s = 0
    r = f[i]
    if g[i] == 0:
        g[i] = 1
    for j in range(i, len(f)):
        if r >= f[j] + 5 and g[j] != 1:
            s = 1
            g[j] = 1
            r = f[j]
    if s == 1:
        n += 1
print(g.count(0))
print(n)
