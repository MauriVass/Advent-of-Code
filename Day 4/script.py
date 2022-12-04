def IsContained(elf1, elf2):
    if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]):
        return True
    return False
def IsOverlapped(elf1, elf2):
    if ( (elf1[0] <= elf2[0] and elf1[1] >= elf2[0]) or (elf1[0] <= elf2[1] and elf1[1] >= elf2[1]) ):
        return True
    return False


f = open('input.txt')
# f = open('example.txt')
pt1 = False

assignment_counter = 0
for line in f.readlines():
    elves_assignments = line[:-1].split(',')
    elf1_assignments = [int(i) for i in elves_assignments[0].split('-')]
    elf2_assignments = [int(i) for i in elves_assignments[1].split('-')]

    if(pt1):
        if (IsContained(elf1_assignments, elf2_assignments) or IsContained(elf2_assignments, elf1_assignments)):
            assignment_counter += 1
    else:
        if (IsOverlapped(elf1_assignments, elf2_assignments) or IsOverlapped(elf2_assignments, elf1_assignments)):
            assignment_counter += 1
print(assignment_counter)  #pt1 550 #pt2 931
f.close()
