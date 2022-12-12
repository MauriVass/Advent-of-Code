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
for i, l in enumerate(string.ascii_lowercase):
    weights[l] = i
nodes = {}

x = 0
y = 0
for line in f.readlines():
    line = line[:-1]
    x = 0
    for l in line:
        if (l == 'S'):
            starting_node = Node((x, y), 0)
            starting_node.distance = 0
            nodes[x, y] = starting_node
        elif (l == 'E'):
            ending_node = Node((x, y), weights['z'])
            # ending_node.distance = np.
            nodes[x, y] = ending_node
        else:
            nodes[x, y] = Node((x, y), weights[l])
        x += 1
    y += 1
width = x
height = y
f.close()


def condition(current_node, node, visited_nodes):
    return current_node.weight + 1 >= node.weight and node not in visited_nodes


nodes_to_visit = list(nodes.values())
visited_nodes = []
current_node = starting_node

while ending_node not in visited_nodes:
    current_node = None
    min = np.inf
    for n in nodes_to_visit:
        if (n.distance < min):
            min = n.distance
            current_node = n

    x = current_node.pos[0]
    y = current_node.pos[1]
    # Top
    if (y - 1 >= 0):
        node = nodes[x, y - 1]
        if (condition(current_node, node, visited_nodes)):
            node.distance = current_node.distance + 1
    # Right
    if (x + 1 < width):
        node = nodes[x + 1, y]
        if (condition(current_node, node, visited_nodes)):
            node.distance = current_node.distance + 1
    # Down
    if (y + 1 < height):
        node = nodes[x, y + 1]
        if (condition(current_node, node, visited_nodes)):
            node.distance = current_node.distance + 1
    # Left
    if (x - 1 >= 0):
        node = nodes[x - 1, y]
        if (condition(current_node, node, visited_nodes)):
            node.distance = current_node.distance + 1
    nodes_to_visit.remove(current_node)
    visited_nodes.append(current_node)

print(ending_node.distance) #pt1 391

