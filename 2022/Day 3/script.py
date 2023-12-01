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

    #Complexity of O(n^2) with n = length_rucksack
    #it can be improved using set(rucksack1) to remove duplicates
    for letter in rucksack1:
        if(letter in rucksack2):
            priorities += mapping_priorities[letter]
            break #break loop
print(priorities) #pt1 8139

f.seek(0)
priorities = 0
rucksacks = [0,0,0]
num_elves = 3
for counter, line in enumerate(f.readlines()):
    rucksacks[counter % num_elves] = line[:-1]
    if(counter%num_elves==2 and counter>0):
        similarities = []

        rucksack1 = rucksacks[0]
        rucksack2 = rucksacks[1]
        for letter in rucksack1:
            if (letter in rucksack2 and letter not in similarities):
                similarities.append(letter)

        rucksack3 = rucksacks[2]
        for s in similarities:
            if (s in rucksack3):
                priorities += mapping_priorities[s]
print(priorities) #pt2 2668

f.close()
