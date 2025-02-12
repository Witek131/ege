f = open('file/demo_2025_27_Б.txt').read().split('\n')
data = []
clusters = []
for line in f[1:]:
    line = line.replace(',', '.')
    p = [float(x) for x in line.split()]
    data.append(p)
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

def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def Claster(p0):
    cluster = [p for p in data if dist(p0, p) < 1.5]
    if len(cluster) > 0:
        for i in cluster:
            data.remove(i)
        next_cluster = [Claster(p) for p in cluster]
        cluster = cluster + sum(next_cluster, [])
    return cluster


while len(data) > 0:
    p0 = data.pop()
    cluster = [p0]+Claster(p0)
    clusters.append(cluster)
sx=0
sy=0
for i in range(len(clusters)):
    sx+= centr(clusters[i])[0]
    sy+= centr(clusters[i])[1]
print(sx/len(clusters)*10000,sy/len(clusters)*10000)
