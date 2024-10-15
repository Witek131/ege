from itertools import *
def f(s1, s2):
    s21=''.join(set(''.join(s2.split())))
    s2 = {frozenset(x) for x in s2.split()}
    for i in permutations(s21):
        s3 = s1
        for j in zip(''.join([str(i+1) for i in range(len(s21))]), i):  # j это все возможные варианты (цифра, буква)
            s3 = s3.replace(j[0], j[1])
        s3 = {frozenset(x) for x in s3.split()}

        if s2 == s3:
            print(' '.join([str(i+1) for i in range(len(s21))]))
            print(*i)

# https://kompege.ru/task 17664
s1 = '248 157 456 136 23 34 28 17'
s2='FBE AEH FGH GH AB CD CDB AC'
f(s1, s2)
# 1 2 3 4 5 6 7 8
# H C A B F E G D (1 в 4 = 2 +2 в 7==21) Ответ 23
# https://kompege.ru/task 17620
s1 = '256 134 267 27 16 135 34'
s2='FB AFD EG BEG FDC ABE CD'
f(s1, s2)
# (1+6)+(2+3) = 55




