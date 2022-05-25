from collections import defaultdict

input = [1,17,0,10,18,11,6]

ndict = defaultdict(list)
for i, x in enumerate(input):
    ndict[x].append(i+1)

last_spoken = input[-1]

for i in range(len(input) + 1, 30000001):
    count = len(ndict[last_spoken])
    if count == 1:
        ndict[0].append(i)
        last_spoken = 0
    else:
        diff = ndict[last_spoken][-1] - ndict[last_spoken][-2]
        ndict[diff].append(i)
        last_spoken = diff

print(last_spoken)
