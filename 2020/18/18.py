#!/usr/bin/env python
import math

dat = open('input.dat').read().replace(' ', '').strip().splitlines()

def calc(eq):
    s = []
    i = 0
    while i < len(eq):
        x = eq[i]
        if x == '(':
            c = 1
            for j, e in enumerate(eq[i+1:]):
                if e == '(': c += 1
                if e == ')': c -= 1
                if c == 0:
                    s.append(calc(eq[i+1:i+j+1]))
                    break
            i += j + 1
        elif x == '*':
            pass
        elif x == '+':
            if eq[i+1] == '(':
                c = 1
                for j, e in enumerate(eq[i+2:]):
                    if e == '(': c += 1
                    if e == ')': c -= 1
                    if c == 0:
                        s.append(calc(eq[i+2:i+j+2]))
                        break
                i += j + 2
                s.append(s.pop() + s.pop())
            else:
                s.append(s.pop() + int(eq[i+1]))
                i += 1
        else:
            s.append(int(x))
        i += 1
    return math.prod(s)

print(sum([calc(x) for x in dat]))
