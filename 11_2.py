from copy import deepcopy

fn = 'input.dat'
rd = open(fn).read().strip().split('\n')
mat1 = [list(x) for x in rd]
mat2 = deepcopy(mat1)
lx = len(mat1[0])
ly = len(mat1)

def isOccupied(d, i, j, f):
    global mat1
    global ly
    global lx
    if f == 0:
        if i == -1 or i == ly or j == -1 or j == lx:
            return 0
        elif mat1[i][j] == 'L':
            return 0
        elif mat1[i][j] == '#':
            return 1
    
    if d == 0:
        return isOccupied(d, i+1, j, 0)
    elif d == 1:
        return isOccupied(d, i-1, j, 0)
    elif d == 2:
        return isOccupied(d, i, j+1, 0)
    elif d == 3:
        return isOccupied(d, i, j-1, 0)
    elif d == 4:
        return isOccupied(d, i+1, j+1, 0)
    elif d == 5:
        return isOccupied(d, i+1, j-1, 0)
    elif d == 6:
        return isOccupied(d, i-1, j+1, 0)
    elif d == 7:
        return isOccupied(d, i-1, j-1, 0)
    assert True, "something is wrong"

def check(i, j):
    return sum([isOccupied(x, i, j, 1) for x in range(8)])

change = 1
while change != 0:
    change = 0
    for i, l in enumerate(mat1):
        for j, x in enumerate(l):
            if x == '.':
                continue
            s = check(i, j)
            if s == 0:
                if mat2[i][j] == 'L':
                    change = 1
                mat2[i][j] = '#'
            elif s >= 5:
                if mat2[i][j] == '#':
                    change = 1
                mat2[i][j] = 'L'
    mat1 = deepcopy(mat2)

ss = ''
for l in mat2:
    ss += ''.join(l)
print(ss.count('#'))
