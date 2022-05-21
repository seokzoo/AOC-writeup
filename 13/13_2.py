import math
from functools import reduce

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(m, a):
    sum = 0
    prod = reduce(lambda acc, b: acc*b, m)
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


ll = open('input.dat').read().strip().split('\n')

timestamp = int(ll[0])
ids = ll[1].split(',')
idx = list(map(int, [i for i, x in enumerate(ids) if x != 'x']))
ids = list(map(int, [x for i, x in enumerate(ids) if x != 'x']))
idx = [-x for x in idx]

print(chinese_remainder(ids, idx))
