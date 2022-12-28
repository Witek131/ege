"""Для игры, описанной в задании 19, найдите такое значение S, при котором
у Вани есть стратегия, позволяющая ему выиграть первым или вторым ходом
при любой игре Пети, но у Вани нет стратегии, которая позволяла бы ему
гарантированно выиграть первым ходом."""


def f(x, p):
    if x >= 103 and (p == 2 or p == 4):
        return True
    else:
        if x < 103 and p == 4:
            return False
        else:
            if x >= 103:
                return False
    if p % 2 == 1:
        if (x + 1) % 3 == 0:
            return f(x + 2, p + 1) or f(x * 2, p + 1)
        elif (x * 2) % 3 == 0:
            return f(x + 2, p + 1) or f(x + 1, p + 1)
        elif (x + 2) % 3 == 0:
            return f(x * 2, p + 1) or f(x + 1, p + 1)
    else:
        if (x + 1) % 3 == 0:
            return f(x + 2, p + 1) and f(x * 2, p + 1)
        elif (x * 2) % 3 == 0:
            return f(x + 2, p + 1) and f(x + 1, p + 1)
        elif (x + 2) % 3 == 0:
            return f(x * 2, p + 1) and f(x + 1, p + 1)


print(f(47, 0))
for i in range(1, 200):
    if f(i, 0) and i % 3 != 0:
        print(i)
