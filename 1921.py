def m(a, b):
    return (a+1, b), (a, b+1,), (a*2, b), (a, b*2)
 
g = [[0]*65*3 for _ in range(65*3)]
for x in range(65, 0, -1):
    for y in range(65, 0, -1):
        if any(70 <= a*b <= 110 for a, b in m(x, y)):
            g[x][y] = 1
        elif g[x][y] == 0 and all(g[a][b] == 1  or\
                                  a + b > 110 for a, b in m(x, y)):
            g[x][y] = 2
        elif g[x][y] == 0 and any(g[a][b] == 2 for a, b in m(x, y)):
            g[x][y] = 3
        elif g[x][y] == 0 and all(g[a][b] in (1, 3) or a + b > 110 \
                                  for a, b in m(x, y)):
            g[x][y] = 4
 
p2 = [x for x in range(1, 66) if g[5][x] == 3]
v2 = [x for x in range(1, 66) if g[5][x] == 4]
print(*p2,' ', min(v2))
