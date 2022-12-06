s = list(map(int, open("i.txt").read().split()[1:]))
f = 0
ss = 0
d = [0] * 999
d[0] = 1
for i in range(len(s)):
    f += s[i]
    ss += d[f % 999]
    d[f % 999] += 1
print(ss)

