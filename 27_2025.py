import math
print(math.ceil(15000/1024))
f = open('file/demo_2025_27_А.txt').read().split('\n')[1:]
def centr(k):
    mc = 10 ** 20
    xc, yc = 0, 0
    for i in range(len(k)):
        x1, y1 = k[i]
        s = 0
        for j in range(len(k)):
            x2, y2 = k[j]
            d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            s += d
        if s < mc:
            mc = s
            xc, yc = x1, y1
    return xc, yc

k1, k2 = [], []
for s in f:
    x, y = map(float, s.replace(',', '.').split())
    if x > -2 and x < 1 and y > 0 and y < 3:
        k1.append((x, y))
    elif x > 1 and x < 5 and y > 3 and y < 7:
        k2.append((x, y))
x1, y1 = centr(k1)
x2, y2 = centr(k2)
print((x1 + x2) / 2 * 10000, (y1 + y2) / 2 * 10000)
f = open('file/demo_2025_27_Б.txt').read().split('\n')[1:]
k1, k2, k3 = [], [], []
for s in f:
    x, y = map(float, s.replace(',', '.').split())
    if x > -1 and x < 3 and y > 0 and y < 3.5:
        k1.append((x, y))
    elif x > 2 and x < 5 and y > 6.5 and y < 11:
        k2.append((x, y))
    elif x > 5 and x < 8 and y > 3.5 and y < 6.5:
        k3.append((x, y))
x1, y1 = centr(k1)
x2, y2 = centr(k2)
x3, y3 = centr(k3)
print((x1 + x2 + x3) / 3 * 10000, (y1 + y2 + y3 ) / 3 * 10000)