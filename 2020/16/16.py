import copy
from collections import defaultdict

dat = open('input.dat').read().strip().split('\n\n')
cond = dat[0].splitlines()
my = list(map(int, dat[1].splitlines()[1].split(',')))
nearby = [list(map(int, x.split(','))) for x in dat[2].split(':\n')[1].splitlines()]

cdict = {}
for x in cond:
    xx = x.split(': ')
    cdict[xx[0]] = '(' + xx[1].replace('-', '<=x<=') + ')'

fail = []
validated = copy.deepcopy(nearby)
for e in nearby:
    for x in e:
        if any([eval(c) for c in cdict.values()]) == 0:
            fail.append(x)
            validated.remove(e)
print(sum(fail))

classified = [[x[i] for x in validated] for i in range(len(validated[0]))]
possible_list = defaultdict(list)

for i in range(len(classified)):
    for k, c in cdict.items():
        if all([eval(c) for x in classified[i]]):
            possible_list[i].append(k)

s = sorted(list(possible_list.items()), key=lambda x: len(x[1]))
dp = 1
prev = []
for x in s:
    if 'departure' in list(set(x[1]) - set(prev))[0]:
        dp *= my[x[0]]
    prev = x[1]
print(dp)
