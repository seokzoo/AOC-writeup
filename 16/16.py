import copy
from collections import defaultdict

dat = open('input.dat').read().strip().split('\n\n')
cond = dat[0].split('\n')
my = list(map(int, dat[1].split('\n')[1].split(',')))
nearby = [list(map(int, x.split(','))) for x in dat[2].split(':\n')[1].split('\n')]

cdict = {}
for x in cond:
    xx = x.split(': ')
    cdict[xx[0]] = '(' + xx[1].replace('-', '<=x<=') + ')'

def validate(x):
    v = 0
    for c in cdict.values():
        if eval(c): v += 1
    if v == 0:
        return 0
    else:
        return 1


validated = copy.deepcopy(nearby)
for x in nearby:
    for k in x:
        if validate(k) == 0:
            validated.remove(x)

classified = [[x[i] for x in validated] for i in range(len(validated[0]))]
possible_list = defaultdict(list)

def validate2(clist, i):
    for k, c in cdict.items():
        v = 0
        for x in clist:
            if not eval(c): break
            v += 1
        if v == len(clist):
            possible_list[i].append(k)

for i in range(len(classified)):
    validate2(classified[i], i)


s = sorted(list(possible_list.items()), key=lambda x: len(x[1]))
dp = 1
prev = []
for x in s:
    if 'departure' in list(set(x[1]) - set(prev))[0]:
        dp *= my[x[0]]
    prev = x[1]
print(dp)
