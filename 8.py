"""Определите количество пятизначных чисел, записанных в восьмеричной
системе счисления, в записи которых только одна цифра 6, при этом никакая
нечётная цифра не стоит рядом с цифрой 6"""
d = ['16', '61', '36', '63', '56', '65', '67', '76']
su = 0
for i in range(8 ** 4, 8 ** 5):
    s = (oct(i)[2:])
    f = 1
    if s.count('6') == 1:
        for j in d:
            if j in s:
                f = 0
                break
        if f:
            su+=1
print(su)
