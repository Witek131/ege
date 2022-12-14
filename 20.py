"""Для игры, описанной в задании 19, укажите два значения S, при которых Петя
не может выиграть первым ходом, но у Пети есть выигрышная стратегия,
позволяющая ему выиграть вторым ходом при любой игре Вани.
В ответе запишите найденные значения в порядке возрастания: сначала
меньшее, затем большее."""


def f(x, p):
    if x >= 103 and p == 3:
        return True
    else:
        if x < 103 and p == 3:
            return False
        if x >= 103 and p % 2 == 0:
            return False
    if p % 2 == 1:
        if x % 3 == 1:
            return f(x + 1, p + 1) and f(x * 2, p + 1)
        else:
            return f(x + 2, p + 1) and f(x * 2, p + 1)
    else:
        if x % 3 == 1:
            return f(x + 1, p + 1) or f(x * 2, p + 1)
        else:
            return f(x + 2, p + 1) or f(x * 2, p + 1)


for i in range(1, 60):
    if f(i, 0) and i % 3 != 0:
        print(i)
