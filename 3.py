a = open('file/3(1).csv').read().split('\n')[1:]
b = open('file/3(2).csv').read().split('\n')[1:]
c = open('file/3(3).csv').read().split('\n')[1:]
a1 = []
for i in c:
    e = i.split(';')
    if i and e[1] == 'Заречный':
        a1.append(e[0])
a2 = {}
for i in b:
    e = i.split(';')
    if i and e[0] not in a2:
        a2[e[0]] = e[2]

a3 = {}
for i in a:
    e = i.split(';')
    if i and e[2] in a1 :
        if e[5] == 'Поступление':
            if e[2] not in a3:
                a3[e[2]] = [a2[e[3]]]
            else:
                a3[e[2]].append(a2[e[3]])
for i in a3:
    print(i)
    for j in a3[i]:
        print(j)
