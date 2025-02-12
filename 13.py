'''
В терминологии сетей TCP/IP маской сети называется двоичное число,
определяющее, какая часть IP-адреса узла сети относится к адресу сети,
а какая – к адресу самого узла в этой сети. При этом в маске сначала
(в старших разрядах) стоят единицы, а затем с некоторого места – нули.
Адрес сети получается в результате применения поразрядной конъюнкции
к заданному IP-адресу узла и маске.
Например, если IP-адрес узла равен 231.32.255.131, а маска равна
255.255.240.0, то адрес сети равен 231.32.240.0.
Узлы с IP-адресами 120.91.176.213 и 120.91.174.205 находятся в одной сети.
Укажите наибольшее возможное значение третьего слева байта маски этой
сети. Ответ запишите в виде десятичного числа.
'''
from ipaddress import *
#print(bin(176)[2:], bin(174)[2:], int('11100000', 2))
for i in range(0, 33):
    for j in range(0, 33):
        nnp1 = ip_network('120.91.176.205'+'/'+str(i),0)
        nnp2 = ip_network('120.91.174.213' + '/' + str(j), 0)
        if nnp1.network_address == nnp2.network_address:
            print(min(nnp1.netmask, nnp2.netmask))
'''
В терминолгии сетей TCP/IP маской сети называют двоичное число, которое показывает, каг
часть IP-адреса узла сети относится к адресу сети, а какая — к адресу узла 1 и сети. Адрес 
сети получается в результате применения поразрядной конъюнкци. данному адресу узла и маске сети.
Сеть задана дресом 23.140.159.160 и маской сети 255.255.252.0. Сколько в этой сети IP-адрес . 
для которых в двоичной записи IP-адреса суммарное количество единиц в левых двух байтах не менее 
суммарного количеств единиц в правых двух байтах.
В ответе укажите только число.
print(bin(23)[2:], bin(140)[2:], bin(159)[2:], bin(160)[2:], bin(252)[2:])
#остается свободным 10 бит или 1024
c=0 
for i in range(1024):
    if bin(i)[2:].count('1') <= 3: #так как 4 уже есть, а должно быть 7
        c+=1
print(c)
'''
