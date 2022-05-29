import copy
from collections import defaultdict

dat = open('input.dat').read().strip().splitlines()

inital_length = len(dat[0])

cdict = defaultdict(lambda:[0, 0]) # c, s

def change(x, f=1):
    for a in [-1, 0, 1]: 
        for b in [-1, 0, 1]: 
            for c in [-1, 0, 1]: 
                for d in [-1, 0, 1]: 
                    if not (a == 0 and b == 0 and c == 0 and d == 0):
                        idx = tuple([x[i] + (a,b,c,d)[i] for i in range(len(x))])
                        cdict[idx][1] = max(0, cdict[idx][1] + f)

for i, x in enumerate(dat):
    for j, k in enumerate(x):
        if k == '#':
            cdict[(j, i, 0, 0)][0] = 1 # x, y, z, w
            change((j, i, 0, 0))
            
for _ in range(6):
    prev = copy.deepcopy(cdict)
    for k, v in prev.items():
        if v[0] == 1:
            if not (v[1] == 2 or v[1] == 3):
                cdict[k][0] = 0 
                change(k, -1)
        else:
            if v[1] == 3:
                cdict[k][0] = 1
                change(k)
    print(sum([x[0] for x in cdict.values()]))
