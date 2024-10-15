# https://kompege.ru/task 17664
from itertools import *

s1 = '248 157 456 136 23 34 28 17'
s2={frozenset(x) for x in 'FBE AEH FGH GH AB CD CDB AC'.split()}
for i in permutations('ABCDEFGH'):
    s3=s1
    for j in zip('12345678', i) :# j это все возможные варианты (цифра, буква)
        s3 =s3.replace(j[0], j[1])
    s3= {frozenset(x) for x in s3.split()}

    if s2 == s3:
        print('1 2 3 4 5 6 7 8')
        print(*i)


