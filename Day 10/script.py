f = open('input.txt')
# f = open('example.txt')

x = 1
current_cycle = 0
signal_strength = 0
cycles_steps = [20, 60, 100, 140, 180, 220]
cycles_steps_seen = 0
is_increment_x = False
for line in f.readlines():
    line = line[:-1].split(' ')
    if(len(line)==1): #noop
        current_cycle+=1
    else: #addx
        is_increment_x=True
        current_cycle += 2

    if(cycles_steps_seen<len(cycles_steps) and current_cycle>=cycles_steps[cycles_steps_seen]):
        signal_strength += x * cycles_steps[cycles_steps_seen]
        cycles_steps_seen += 1

    if(is_increment_x):
        x+=int(line[1])
        is_increment_x=False


print(signal_strength) #pt1 16880
f.close()
