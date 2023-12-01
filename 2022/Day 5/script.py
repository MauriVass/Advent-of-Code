def MoveCrates(ship, index, from_stack, to_stack, pt1):
    crates_to_move = index
    if(pt1==True):
        for _ in range(crates_to_move):
            crate = ship[from_stack].pop()
            ship[to_stack].append(crate)
    else:
        tmp = ship[from_stack][-index:]
        ship[from_stack] = ship[from_stack][:-index]
        [ship[to_stack].append(t) for t in tmp]


f = open('input.txt')
# f = open('example.txt')
pt1 = True

ship = {}
num_crates = 9 #3 for example.txt
for i in range(num_crates):
    ship[i + 1] = []
crates_allocation = True

assignment_counter = 0
for line in f.readlines():
    if(line=='\n'):
        crates_allocation = False
    if(crates_allocation):
        for index in range(len(line[:-1])):
            if(line[index]=='['):
                ship[int(index / 4)+1].insert(0, line[index + 1])
    elif(line!='\n'):
        elements = line[:-1].split(' ')
        index_crate = int(elements[1])
        from_stack = int(elements[3])
        to_stack = int(elements[5])

        MoveCrates(ship, index_crate, from_stack, to_stack, pt1)

message = ''
for index_crate in range(num_crates):
    message += ship[index_crate+1][-1]
print(message) #pt1 SBPQRSCDF pt2 RGLVRCQSB
f.close()

