f = open('input.txt')
# f = open('example.txt')

#Pt 1
x = 1
current_cycle = 0
signal_strength = 0
cycles_steps = [20, 60, 100, 140, 180, 220]
cycles_steps_seen = 0
is_increment_x = False

for line in f.readlines():
    line = line[:-1].split(' ')
    if(len(line)==1): #noop
        current_cycle += 1
    else: #addx
        is_increment_x=True
        current_cycle += 2

    #Part 1
    if(cycles_steps_seen<len(cycles_steps) and current_cycle>=cycles_steps[cycles_steps_seen]):
        signal_strength += x * cycles_steps[cycles_steps_seen]
        cycles_steps_seen += 1

    if(is_increment_x):
        x+=int(line[1])
        is_increment_x=False
print(signal_strength) #pt1 16880

#Pt 2
def operations(current_cycle, CRT_pos, image):
    current_cycle += 1
    distance = CRT_pos - x
    if (distance >= -1 and distance <= 1):
        image += '#'
    else:
        image += '.'
    CRT_pos += 1

    if (current_cycle % CRT_max_width == 0):
        image += '\n'
        CRT_pos = 0
    return current_cycle, CRT_pos, image
f.seek(0)
x = 1
current_cycle = 0
image = ''
CRT_max_width = 40
current_CRT_pos = 0
for line in f.readlines():
    line = line[:-1].split(' ')
    current_cycle, current_CRT_pos, image = operations(current_cycle, current_CRT_pos, image)
    if (len(line) == 2):
        current_cycle, current_CRT_pos, image = operations(current_cycle, current_CRT_pos, image)
        x += int(line[1])



print(image)
ff = open('sol_pt2.txt', 'w')
ff.write(image)
ff.close()
f.close()
