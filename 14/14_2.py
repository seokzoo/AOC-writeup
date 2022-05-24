import itertools
from collections import defaultdict

ll = open('input.dat').read().strip().split('\n')

mem = defaultdict(lambda :0)
mask = ''
count = 0

for l in ll:
    parsed = l.split(' = ')
    if parsed[0] == 'mask':
        mask = parsed[1]
        count = parsed[1].count('X')
    else:
        addr = list(str(bin(int(parsed[0][4:-1])))[2:].zfill(36))
        if mask != '':
            for i, x in enumerate(mask):
                if x == 'X':
                    addr[i] = 'X'
                elif x == '1':
                    addr[i] = '1'
        permutations = list(itertools.product([0, 1], repeat=count))
        for i in range(len(permutations)):
            masked = eval('0b' + ''.join(addr).replace('X', '{}').format(*permutations[i]))
            mem[masked] = int(parsed[1])

print(sum(mem.values()))
