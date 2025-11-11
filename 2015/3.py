s = set()
with open("data") as f:
    cur1 = [0, 0]
    cur2 = [0, 0]
    while (l := f.readline()):
        s.add('0_0')
        for i, d in enumerate(l):
            if i % 2 == 0:
                if d == '>':
                    cur1[0] += 1
                elif d == '<':
                    cur1[0] -= 1
                elif d == '^':
                    cur1[1] += 1
                elif d == 'v':
                    cur1[1] -= 1
                s.add(f'{cur1[0]}_{cur1[1]}')
            else:
                if d == '>':
                    cur2[0] += 1
                elif d == '<':
                    cur2[0] -= 1
                elif d == '^':
                    cur2[1] += 1
                elif d == 'v':
                    cur2[1] -= 1
                s.add(f'{cur2[0]}_{cur2[1]}')

print(len(s))
