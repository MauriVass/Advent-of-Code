import string
def Generate_priorities():
    priorities = {}

    value = 1
    for i in string.ascii_letters:
        priorities[i] = value
        value+=1
    return priorities

f = open('input.txt')

mapping_priorities = Generate_priorities()

priorities = 0
for line in f.readlines():
    length_rucksack = int(len(line[:-1])/2)
    rucksack1 = line[:length_rucksack]
    rucksack2 = line[length_rucksack:-1]

    #Complexity of O(length_rucksack^2) in the worst case
    #it can be improved using set(rucksack1) to remove duplicates
    for letter in rucksack1:
        if(letter in rucksack2):
            priorities += mapping_priorities[letter]
            break #break loop
print(priorities) #pt1 8139
f.close()
