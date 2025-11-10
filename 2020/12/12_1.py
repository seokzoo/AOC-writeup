rd = open('12_1.dat').read().strip().split('\n')

class ship():
    degree = 0 # east
    x = 0
    y = 0
    def show(self):
        print(self.x, self.y)
        print(abs(self.x) + abs(self.y))
    def N(self, value):
        self.y += value
    def S(self, value):
        self.y -= value
    def E(self, value):
        self.x += value
    def W(self, value):
        self.x -= value
        
    def L(self, deg):
        self.degree -= deg
        self.degree %= 360
        
    def R(self, deg):
        self.degree += deg
        self.degree %= 360
        
    def F(self, value):
        if self.degree == 0:
            self.E(value)
        elif self.degree == 90:
            self.S(value)
        elif self.degree == 180:
            self.W(value)
        elif self.degree == 270:
            self.N(value)

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
