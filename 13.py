from ipaddress import *

print(bin(176)[2:], bin(174)[2:], int('11100000', 2))
for i in range(0, 33):
    np = ip_network('120.91.176.205/' + str(i), 0)
    mas = str(np).split('/')
    if mas[0] == '120.91.174.205':
        print(np, np.netmask)
