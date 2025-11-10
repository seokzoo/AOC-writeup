from collections import defaultdict

ll = open('input.dat').read().strip().split('\n')

mem = defaultdict(lambda :0)
mask = lambda x: x

for l in ll:
    parsed = l.split(' = ')
    if parsed[0] == 'mask':
        orMask = eval('0b' + parsed[1].replace('X', '0'))
        andMask = eval('0b' + parsed[1].replace('X', '1'))
        mask = lambda x: (x | orMask) & andMask
    else:
        masked = mask(int(parsed[1]))
        mem[int(parsed[0][4:-1])] = masked

print(sum(mem.values()))
