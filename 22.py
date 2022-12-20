f = open("file/22.csv").read().split('\n')[1:]
s1 = []
s2 = []
s3 = []
for i in range(len(f)):
    a = f[i].split(';')
    print(a)
    if a[0]:
        s1.append(int(a[0]))
        s2.append(int(a[1]))
        if len(a) == 3:
            s3.append([a[2]])
        else:
            a[2] = a[2][1:]
            a[-1] = a[-1][:-1]
            s3.append(' '.join(a[2:]).split())
        # print(s3)
s4 = []
# print(s3)
for i in range(len(s3)):
    mabv = -1
    for j in range(len(s3[i])):
        # print(s3[i])
        if len(s3[i][j]) == 1 and s3[i][j] == '0':
            mabv = int(s2[i])
        elif len(s3[i]) == 1:
            mabv = s4[int(s3[i][j]) - 1] + int(s2[i])
        else:
            if s4[int(s3[i][j]) - 1] > mabv:
                mabv = int(s4[int(s3[i][j]) - 1])
    if len(s3[i][j]) == 1 and s3[i][j] == '0':
        s4.append(mabv)
    elif len(s3[i]) == 1:
        s4.append(mabv)
    else:
        s4.append(mabv + int(s2[i]))

print(max(s4), s4[-1], s4)