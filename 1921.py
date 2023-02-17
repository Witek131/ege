'''"После того, как все подарки были развезены, Дед Мороз со Снегурочкой решили отдохнуть и сыграть в игру. Перед ними лежат две кучи со снежками, и ходят они по очереди, первый ход делает Снегурочка. За один ход игрок может добавить в одну из куч (по своему выбору) один снежок или увеличить количество снежков в куче в два раза. Например, пусть в одной куче 10 камней, а в другой 5 снежков; такую позицию в игре будем обозначать (10, 5). Тогда за один ход можно получить любую из четырёх позиций: (11, 5), (20, 5), (10, 6), (10, 10). Для того чтобы делать ходы, у каждого игрока есть неограниченное количество снежков. Игра завершается в тот момент, когда произведение количества снежков в кучах становится не менее 70. Если при этом произведение оказалось не более 110, то победителем считается игрок, сделавший последний ход. В противном случае победителем становится его противник. В начальный момент в первой куче было пять камней, во второй куче – S камней; 1 ≤ S ≤ 65. Известно, что Дед Мороз выиграл своим первым ходом после неудачного первого хода Снегурочки. Укажите минимальное значение S, когда такая ситуация возможна.

Задание 20.
Для игры, описанной в предыдущем задании, найдите два наименьших значения S, при которых у Снегурочки есть
выигрышная стратегия, причём одновременно выполняются два условия:
− Снегурочка не может выиграть за один ход;
− Снегурочка может выиграть своим вторым ходом независимо от того, как будет ходить Дед Мороз.
Найденные значения запишите в ответе в порядке возрастания.

Задание 21.
Для игры, описанной в задании 19, найдите минимальное значение S, при котором одновременно выполняются два условия:
– у Деда Мороза есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Снегурочки;
– у Деда Мороза нет стратегии, которая позволит ему гарантированно выиграть первым ходом."'''
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
