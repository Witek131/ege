"""Для игры, описанной в задании 19, найдите такое значение S, при котором
у Вани есть стратегия, позволяющая ему выиграть первым или вторым ходом
при любой игре Пети, но у Вани нет стратегии, которая позволяла бы ему
гарантированно выиграть первым ходом."""
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