import math
import matplotlib.pyplot as plt

def parse(s):
    return [(x[0], int(x[1:])) for x in s.split(';')]
# [('R', 3), ('R', 4), ('F', 100), ('T', 90), ('E', 0), ('F', 100), ('E', 0)]
class Maker:
    def __init__(self):
        self.x, self.y, self.angle = 0, 0, 0
        plt.xlim(-320, 320)
        plt.ylim(-240, 240)
    
    def forward(self, val):
        print(val)
        rad = math.radians(self.angle)
        print(rad)
        dx = val * math.cos(rad)
        dy = val * math.sin(rad)
        print(dx)
        print(dy)
        x1, y1, x2, y2 = self.x, self.y, self.x + dx, self.y + dy
        plt.plot([x1, x2], [y1, y2], color='black', linewidth=2)
        self.x, self.y = x2, y2
    
    def turn(self, val):
        print("val",val)
        print(self.angle)
        self.angle = (self.angle + val) % 360
        print(self.angle)

    def show(self):
        plt.show()

def draw(s):
    insts = parse(s)
    marker = Maker()
    stack = []
    opno = 0
    while opno < len(insts):
        print(stack)
        code, val = insts[opno]
        if code == 'F':
            marker.forward(val)
        elif code == 'T':
            marker.turn(val)
        elif code == 'R':
            stack.append({'opno': opno, 'rest':val})
        elif code == 'E':
            if stack[-1]['rest'] > 1:
                opno = stack[-1]['opno']
                stack[-1]['rest'] -= 1
            else:
                stack.pop()
        opno += 1
    marker.show()

