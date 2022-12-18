class Shape:
    def __init__(self, height):
        self.elements = []
        self.height = height

    def getMaxHeight(self):
        return self.elements[0][1]

    def moveDown(self):
        for e in self.elements:
            e[1] -= 1
    def moveUp(self):
        for e in self.elements:
            e[1] += 1

shift = 4
width = 7
class LineH(Shape):
    def __init__(self, height):
        self.elements = [[2,height+shift], [3, height+shift], [4, height+shift], [5, height+shift]]
    def moveRight(self):
        for e in self.elements:
            e[0] += 1
        acceptable_move = checkCollisions(self.elements)
        if(acceptable_move == False or self.elements[-1][0] >= width):
            for e in self.elements:
                e[0] -= 1 #Revert changes
    def moveLeft(self):
        for e in self.elements:
            e[0] -= 1
        acceptable_move = checkCollisions(self.elements)
        if (acceptable_move == False or self.elements[0][0] < 0):
            for e in self.elements:
                e[0] += 1  # Revert changes
class Star(Shape):
    def __init__(self, height):
        self.elements = [                    [3, height+shift+2],
                         [2,height+shift+1], [3, height+shift+1], [4, height+shift+1],
                                             [3, height+shift]]
    def moveRight(self):
        for e in self.elements:
            e[0] += 1
        acceptable_move = checkCollisions(self.elements)
        if (acceptable_move == False or self.elements[3][0] >= width):
            for e in self.elements:
                e[0] -= 1  # Revert changes
    def moveLeft(self):
        for e in self.elements:
            e[0] -= 1
        acceptable_move = checkCollisions(self.elements)
        if (acceptable_move == False or self.elements[1][0] < 0):
            for e in self.elements:
                e[0] += 1  # Revert changes
class L(Shape):
    def __init__(self, height):
        self.elements = [                                   [4,height+shift+2],
                                                            [4,height+shift+1],
                         [2, height+shift],[3, height+shift],[4, height+shift]]
    def moveRight(self):
        for e in self.elements:
            e[0] += 1
        acceptable_move = checkCollisions(self.elements)
        if (acceptable_move == False or self.elements[0][0] >= width):
            for e in self.elements:
                e[0] -= 1  # Revert changes
    def moveLeft(self):
        for e in self.elements:
            e[0] -= 1
        acceptable_move = checkCollisions(self.elements)
        if (acceptable_move == False or self.elements[2][0] < 0):
            for e in self.elements:
                e[0] += 1  # Revert changes
class LineV(Shape):
    def __init__(self, height):
        self.elements = [[2,height+shift+3],
                         [2, height+shift+2],
                         [2, height+shift+1],
                         [2, height+shift]]
    def moveRight(self):
        for e in self.elements:
            e[0] += 1
        acceptable_move = checkCollisions(self.elements)
        if (acceptable_move == False or self.elements[-1][0] >= width):
            for e in self.elements:
                e[0] -= 1  # Revert changes
    def moveLeft(self):
        for e in self.elements:
            e[0] -= 1
        acceptable_move = checkCollisions(self.elements)
        if (acceptable_move == False or self.elements[0][0] < 0):
            for e in self.elements:
                e[0] += 1  # Revert changes
class Box(Shape):
    def __init__(self, height):
        self.elements = [[2,height+shift+1], [3, height+shift+1],
                         [2,height+shift], [3, height+shift]]
    def moveRight(self):
        for e in self.elements:
            e[0] += 1
        acceptable_move = checkCollisions(self.elements)
        if (acceptable_move == False or self.elements[1][0] >= width):
            for e in self.elements:
                e[0] -= 1  # Revert changes
    def moveLeft(self):
        for e in self.elements:
            e[0] -= 1
        acceptable_move = checkCollisions(self.elements)
        if (acceptable_move == False or self.elements[0][0] < 0):
            for e in self.elements:
                e[0] += 1  # Revert changes

def checkCollisions(elements):
    for e in elements:
        if(e in pieces or e[1] == 0):
            return False
    return True

def printCave(elem=None):
    for h in range(height + shift + 2, -1, -1):
        m = ''
        for w in range(width):
            if(h == 0):
                m += '-'
            else:
                if([w,h] in pieces):
                    m+= '#'
                elif(elem != None and [w,h] in elem.elements):
                    m+= '@'
                else:
                    m += '.'
        print(m)
    print()

f = open('input.txt')
# f = open('example.txt')

for line in f.readlines():
    line = line[:-1]
f.close()

height = 0
element_counter = 0
len_text = len(line)
pieces = []
wind_counter = 0
debug = False
for round in range(2022):
    element = element_counter % 5
    if(element == 0):
        s = LineH(height)
    elif(element == 1):
        s = Star(height)
    elif(element == 2):
        s = L(height)
    elif(element == 3):
        s = LineV(height)
    else:
        s = Box(height)

    falling = True
    while falling == True:
        if(debug):
            printCave(s)
        direction = line[wind_counter % len_text]
        if(direction == '>'):
            s.moveRight()
        else:
            s.moveLeft()
        if(debug):
            printCave(s)
        s.moveDown()
        falling = checkCollisions(s.elements)
        if(falling==False):
            s.moveUp()
            [pieces.append(ee) for ee in s.elements if ee not in pieces]
        if(debug):
            printCave(s)
        wind_counter += 1
    if(s.getMaxHeight() > height):
        height = s.getMaxHeight()
    if(debug or False):
        printCave()
    element_counter += 1
print(height) #pt1 3235

