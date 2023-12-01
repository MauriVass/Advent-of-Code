f = open('input.txt')
# f = open('example.txt')

rocks = []
mins = [1000,1000]
maxs = [0,0]
for line in f.readlines():
    line = line[:-1].split(' -> ')
    prev_pos = [0,0]
    for l in line:
        x,y = [int(i) for i in l.split(',')]
        if(prev_pos != [0,0]):
            delta_x = x - prev_pos[0]
            if(delta_x>0):
                [rocks.append([prev_pos[0] + xx, y]) for xx in range(delta_x + 1)]
            elif(delta_x<0):
                [rocks.append([prev_pos[0] - xx, y]) for xx in range(-delta_x + 1)]

            delta_y = y - prev_pos[1]
            if(delta_y>0):
                [rocks.append([x, prev_pos[1] + yy]) for yy in range(delta_y + 1)]
            elif (delta_y < 0):
                [rocks.append([x, prev_pos[1] - yy]) for yy in range(-delta_y + 1)]
        prev_pos = [x,y]

        if(x<mins[0]):
            mins[0] = x
        elif(x>maxs[0]):
            maxs[0] = x

        if(y<mins[1]):
            mins[1] = y
        elif(y>maxs[1]):
            maxs[1] = y

print(mins, maxs)
f.close()

reservoir = {}

shift = 6
starting_pos = [500,mins[1]-shift]
for y in range(maxs[1]-mins[1]+1+shift):
    for x in range(maxs[0]-mins[0]+1):
        m = ''
        xx = mins[0] + x
        yy = mins[1] + y - shift
        if([xx, yy] in rocks):
            m = '#'
        else:
            m = '.'
        # if([xx, yy + shift] == starting_pos):
        #     m = '+'
        reservoir[xx, yy] = m

def printReservoir():
    for y in range(maxs[1] - mins[1] + 1 + shift):
        tmp = ''
        for x in range(maxs[0] - mins[0] + 1):
            xx = mins[0] + x
            yy = mins[1] + y - shift
            m = reservoir[xx, yy]
            # tmp += f'{m}({xx%494},{yy})'
            tmp += f'{m}'
        print(tmp)
    print()
printReservoir()

keep_sanding = True
def checkEmptiness(sand):
    counter = 0
    while True:
        new_y = sand[1] + counter
        d = reservoir[sand[0], new_y + 1]
        if (d in ['o', '#']):
            x_l = sand[0] - 1
            if(x_l < mins[0]):
                return False
            l = reservoir[x_l, new_y + 1]
            if (l not in ['o', '#']):
                v = checkEmptiness([x_l, new_y + 1])
                return v
            else:
                x_r = sand[0] + 1
                if (x_r > maxs[0]):
                    return False
                r = reservoir[x_r, new_y + 1]
                if (r not in ['o', '#']):
                    v = checkEmptiness([x_r, new_y + 1])
                    return v
            reservoir[sand[0], new_y] = 'o'
            # printReservoir()
            return True
        counter+=1

num_sands = 0
while keep_sanding:
    sand = starting_pos
    keep_sanding = checkEmptiness(sand)
    if(keep_sanding):
        num_sands += 1

print(num_sands) #pt1 913
