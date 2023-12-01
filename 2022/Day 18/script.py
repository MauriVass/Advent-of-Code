def checkNewCube(cube, dir):
    cube = (c[0] + dir[0], c[1] + dir[1], c[2] + dir[2])
    if(cube in cubes):
        return False
    return True
f = open('input.txt')
# f = open('example.txt')

cubes = []

for line in f.readlines():
    line = line[:-1]
    coords = [int(i) for i in line.split(',')]
    cubes.append((coords[0],coords[1],coords[2]))
f.close()

surface = 0
for c in cubes:
    surface = surface + 1 if checkNewCube(c, (1,0,0)) else surface
    surface = surface + 1 if checkNewCube(c, (-1,0,0)) else surface

    surface = surface + 1 if checkNewCube(c, (0,1,0)) else surface
    surface = surface + 1 if checkNewCube(c, (0,-1,0)) else surface

    surface = surface + 1 if checkNewCube(c, (0,0,1)) else surface
    surface = surface + 1 if checkNewCube(c, (0,0,-1)) else surface
print(surface) #pt1 3636

