import re
import time
def manhattanDistance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

f = open('input.txt')
# f = open('example.txt')

mins = [10**10, 10**10]
maxs = [0,0]
impossible_beacon_pos = set()
t1 = time.time()
y_to_consider = 2000000 #test: 10, pt1: 2000000

for line in f.readlines():
    line = line[:-1]
    elements = re.findall(r'-?\d+', line)
    pos_s = (int(elements[0]), int(elements[1]))
    pos_b = (int(elements[2]), int(elements[3]))
    d = manhattanDistance(pos_s, pos_b)

    dist_to_bacon_row = abs(y_to_consider - pos_s[1])
    num_steps_left = d - dist_to_bacon_row

    if num_steps_left > 0:
        for x in range(pos_s[0] - num_steps_left, pos_s[0] + num_steps_left + 1):
            pos = (x, y_to_consider)
            if pos != pos_b:
                impossible_beacon_pos.add(pos)
f.close()

print(len(impossible_beacon_pos)) #low 4401167
t2 = time.time()
print(f'Time elapsed: {(t2-t1):.1f}')
