from copy import deepcopy

rd = open('12_1.dat').read().strip().split('\n')

class ship():
    degree = 0 # east
    x = 10 # waypoint
    y = 1
    rx = 0 # ship
    ry = 0
    def show(self):
        print(self.rx, self.ry)
        print(abs(self.rx) + abs(self.ry))
    def N(self, value):
        self.y += value
    def S(self, value):
        self.y -= value
    def E(self, value):
        self.x += value
    def W(self, value):
        self.x -= value
        
    def L(self, deg):
        tempx = self.x
        tempy = self.y
        if deg == 90:
            self.y = tempx
            self.x = -tempy
        elif deg == 180:
            self.x = -tempx
            self.y = -tempy
        elif deg == 270:
            self.y = -tempx
            self.x = tempy
    def R(self, deg):
        tempx = self.x
        tempy = self.y
        if deg == 90:
            self.x = tempy
            self.y = -tempx
        elif deg == 180:
            self.x = -tempx
            self.y = -tempy
        elif deg == 270:
            self.x = -tempy
            self.y = tempx
    def F(self, value):
        self.rx += (self.x*value)
        self.ry += (self.y*value)


s = ship()
for l in rd:
    op = l[0:1]
    operand = int(l[1:])
    
    if op == 'N':
        s.N(operand)
    elif op == 'S':
        s.S(operand)
    elif op == 'E':
        s.E(operand)
    elif op == 'W':
        s.W(operand)
    elif op == 'L':
        s.L(operand)
    elif op == 'R':
        s.R(operand)
    elif op == 'F':
        s.F(operand)
        
s.show()
