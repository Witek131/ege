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
            su += 1
print(su)

""""(С. Чайкин) Все шестибуквенные слова, составленные из букв слова РЕКУРСИЯ, записаны в алфавитном порядке и
пронумерованы.
Ниже приведено начало списка.
1. ЕЕЕЕЕЕ
2. ЕЕЕЕЕИ
3. ЕЕЕЕЕК
4. ЕЕЕЕЕР
5. ЕЕЕЕЕС
6. ЕЕЕЕЕУ
Определите количество слов с чётными номерами, которые не начинаются на букву К и содержат не более 2 гласных."""
v = 0
d = 'еуия'
f1 = 0
for i in 'еикрсуя':
    for j in 'еикрсуя':
        for e in 'еикрсуя':
            for r in 'еикрсуя':
                for t in 'еикрсуя':
                    for y in 'еикрсуя':
                        f1 += 1
                        if f1 % 2 != 0:
                            e1 = 0
                            a = i + j + e + r + t + y
                            if a[0] != 'к':
                                for h in a:
                                    if h in d:
                                        e1 += 1
                                if e1 <= 2:
                                    # print(a)
                                    v += 1
print(v)
