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
