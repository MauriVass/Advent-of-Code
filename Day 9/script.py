import math
def changePosition(start, movement):
    new_pos = [0,0]
    new_pos[0] = start[0] + movement[0]
    new_pos[1] = start[1] + movement[1]
    return new_pos
def calculateDistance(head,tail):
    distance = math.fabs(head[0]-tail[0]) + math.fabs(head[1]-tail[1])
    return distance
def changeTailPos(head,tail):
    distance = calculateDistance(head, tail)
    move = False
    if(tail[0] != head[0] and tail[1] != head[1]):
        if(distance>2):
            move = True
    else:
        if(distance>1):
            move = True
    return move

f = open('input.txt')
# f = open('example.txt')

head_pos = [0,0]
tail_pos = [0,0]
visited_position = []
visited_position.append(head_pos)
commands = {'U':[0, 1], 'R':[1, 0], 'D':[0, -1], 'L':[-1, 0]}

for line in f.readlines():
    line = line[:-1].split(' ')
    command = line[0]
    distance = int(line[1])

    for d in range(1, distance+1):
        vector = commands[command]

        head_pos = changePosition(head_pos, vector)
        if(changeTailPos(head_pos,tail_pos)):
            tail_pos = changePosition(head_pos, [-vector[0],-vector[1]])

        if (tail_pos not in visited_position):
            visited_position.append(tail_pos)
print(len(visited_position)) #pt1 6212
f.close()






