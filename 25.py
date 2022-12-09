# Задание 25


def delin(n):
    a = []
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            a.append(i)
            a.append(n // i)
    a.sort()
    return a


s = 710017
a = []
g = []
while len(a) != 5:
    d = delin(s)
    r = s
    n1 = n2 = 0
    for i in range(len(d)):
        if abs(d[i] - s ** 0.5) < r:
            n1 = d[i]
            r = abs(d[i] - s ** 0.5)
            n2 = i
    if len(d) > 1:
        d.pop(n2)

    n3 = 0
    r = s
    for i in range(len(d)):
        if abs(d[i] - s ** 0.5) < r and d[i] > n1:
            n3 = d[i]
            r = abs(d[i] - s ** 0.5)

    #
    if (n1 + n3) % 10 == 0 and n1 * n3 == s:
        if len(a) == 0:
            a.append(s)
            g.append(n1 + n3)
            print(n1, n3, d, s)
        elif n1 + n3 > g[-1]:
            a.append(s)
            g.append(n1 + n3)

    s += 1

print(a, g)
