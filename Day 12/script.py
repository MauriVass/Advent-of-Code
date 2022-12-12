import numpy as np
import string
class Node:
    def __init__(self, pos, weight):
        self.pos = pos
        self.weight = weight
        self.distance = np.inf

f = open('input.txt')
# f = open('example.txt')

weights = {}
for i,l in enumerate(string.ascii_lowercase):
    weights[l] = i
nodes = {}

x = 0
y = 0
for line in f.readlines():
    line = line[:-1]
    x = 0
    for l in line:
        if(l=='S'):
            starting_node = Node((x,y),0)
            starting_node.distance = 0
        elif(l=='E'):
            ending_node = Node((x,y),-1)
            ending_node.distance = -1
        else:
            nodes[x,y] = Node((x,y), weights[l])
            x+=1
    y+=1
height = y
width = x
print(x,y)
f.close()

elements_to_visit = [starting_node]
for current_node in elements_to_visit:
    if(current_node.distance==-1):
        break
    x = current_node.pos[0]
    y = current_node.pos[1]
    #Top
    if(y - 1 >= 0):
        node = nodes[x, y-1]
        if(current_node.weight>=node.weight and node.distance == np.inf and node.distance > current_node.distance + node.weight):
            node.distance = current_node.distance + node.weight
            elements_to_visit.append(node)
    # Right
    if (x + 1 < width):
        node = nodes[x+1, y]
        if(current_node.weight>=node.weight and node.distance == np.inf and node.distance > current_node.distance + node.weight):
            node.distance = current_node.distance + node.weight
            elements_to_visit.append(node)
    # Down
    if (y + 1 < height):
        node = nodes[x, y + 1]
        if(current_node.weight>=node.weight and node.distance == np.inf and node.distance > current_node.distance + node.weight):
            node.distance = current_node.distance + node.weight
            elements_to_visit.append(node)
    # Left
    if (x-1 >= 0):
        node = nodes[x-1, y]
        if(current_node.weight>=node.weight and node.distance == np.inf and node.distance > current_node.distance + node.weight):
            node.distance = current_node.distance + node.weight
            elements_to_visit.append(node)

elements_to_visit = [starting_node]
for current_node in elements_to_visit:
    x = current_node.pos[0]
    y = current_node.pos[1]
    min_distance = 0
    min_distance_node = None
    #Top
    if(y - 1 >= 0):
        node = nodes[x, y-1]
        if(min_distance>node.distance):
            min_distance = node.distance
            min_distance_node = node
    # Right
    if (x + 1 < width):
        node = nodes[x+1, y]
        if(min_distance>node.distance):
            min_distance = node.distance
            min_distance_node = node
    # Down
    if (y + 1 < height):
        node = nodes[x, y+1]
        if(min_distance>node.distance):
            min_distance = node.distance
            min_distance_node = node
    # Left
    if (x-1 >= 0):
        node = nodes[x-1, y]
        if(min_distance>node.distance):
            min_distance = node.distance
            min_distance_node = node
    elements_to_visit.append(node)

print(len(elements_to_visit))

# print(maxs[0] * maxs[1])  # pt1 62491, pt2 17408399184
