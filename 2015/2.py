ans = 0
ans2 = 0
with open("data") as f:
    while (l := f.readline()):
        a, b, c = map(int, l.split('x'))
        ans2 += a*b*c
        ans2 += (a + b + c - max([a, b, c])) * 2
        sides = [a*b, b*c, a*c]
        ans += min(sides)
        for side in sides:
            ans += side * 2
print(ans)
print(ans2)
