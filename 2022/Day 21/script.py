f = open('input.txt')
# f = open('example.txt')

monkeys = {}
for i,line in enumerate(f.readlines()):
    line = line[:-1].split(':')
    monkey = line[0]
    op = line[1].split(' ')[1:]
    if(len(op) == 1):
        monkeys[monkey] = float(op[0])
    else:
        monkeys[monkey] = op

f.close()

keep_searching = True
while keep_searching:
    for k,v in monkeys.items():
        if(type(v) != float):
            monkey1 = v[0]
            monkey2 = v[2]
            if(type(monkeys[monkey1]) == float and type(monkeys[monkey2]) == float):
                if(v[1] == '+'):
                    monkeys[k] = monkeys[monkey1] + monkeys[monkey2]
                elif(v[1] == '-'):
                    monkeys[k] = monkeys[monkey1] - monkeys[monkey2]
                elif(v[1] == '*'):
                    monkeys[k] = monkeys[monkey1] * monkeys[monkey2]
                elif(v[1] == '/'):
                    monkeys[k] = monkeys[monkey1] / monkeys[monkey2]
        if(type(monkeys['root']) == float):
            keep_searching = False
            break
print(monkeys['root']) #pt1 158661812617812

