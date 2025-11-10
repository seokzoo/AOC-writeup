ans = 0
found = False
with open('data') as f:
    for i, x in enumerate(f.read()):
        if x == '(':
            ans += 1
        elif x == ')':
            ans -= 1
        if (not found and ans < 0):
            found = True
            print(i+1)
print(ans)
