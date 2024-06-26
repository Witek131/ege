"""Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит
куча камней. Игроки ходят по очереди, первый ход делает Петя. За один ход
игрок может добавить в кучу один камень, добавить два камня или
увеличить количество камней в куче в два раза. При этом не разрешается
делать ход, после которого количество камней в куче будет делиться на 3
Например, если в начале игры в куче 4 камня, Петя может первым ходом
получить кучу из 5 или из 8 камней. Добавить два камня Петя не может, так как
в этом случае в куче станет 6 камней, а 6 делится на 3
Игра завершается, когда количество камней в куче становится не менее 103
Победителем считается игрок, сделавший последний ход, то есть первым
получивший кучу, в которой будет 103 или больше камней.
В начальный момент в куче было S камней, 1 ≤ S ≤ 101, S не делится на 3
Будем говорить, что игрок имеет выигрышную стратегию, если он может
выиграть при любых ходах противника.
Укажите такое значение S, при котором Петя не может выиграть за один ход,
но при любом ходе Пети Ваня сможет выиграть своим первым ходом."""


def f(x, p):
    if x >= 103 and p == 2:
        return True
    else:
        if x < 103 and p == 2:
            return False
    if p%2 != 0:
        if x % 3 == 1:
            return f(x + 1, p + 1) or f(x * 2, p + 1)
        else:
            return f(x + 2, p + 1) or f(x * 2, p + 1)
    else:
        if x % 3 == 1:
            return f(x + 1, p + 1) and f(x * 2, p + 1)
        else:
            return f(x + 2, p + 1) and f(x * 2, p + 1)

for i in range(1, 500):
    if f(i, 0) and i % 3 != 0:
        print(i)
        break
"""Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок
может добавить в кучу один камень или увеличить количество камней в куче в два раза. Для того чтобы делать ходы, у каждого игрока есть неограниченное
количество камней.
Игра завершается в тот момент, когда количество камней в куче становится не менее 129. Победителем считается игрок, сделавший последний ход, т.е. первым
получивший кучу из 129 или больше камней.
В начальный момент в куче было $ камней, 1 < $ < 128.
Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
Укажите минимальное значение $, при котором Петя не может выиграть за один ход, но при любом ходе Пети Ваня может выиграть своим первым ходом.

def f(x, p):
    if x >= 129 and p == 2:
        return True
    elif x < 129 and p == 2:
        return False
    if p==1:
        return f(x + 1, p + 1) and f(x * 2, p + 1)
    else:
        return f(x * 2, p + 1)


for i in range(1, 500):
    if f(i, 0):
        print(i)
"""