f = open('input.txt')
# f = open('example.txt')
pt1 = False

start_of_packet_marker_index = 0
characters = []
length_starter = 4 if pt1 else 14
for index, character in enumerate(f.read()):
    if(index>=length_starter):
        characters.pop(0)
    characters.append(character)
    if(len(set(characters))==length_starter):
        start_of_packet_marker_index = index+1
        break

print(start_of_packet_marker_index) #pt1 1920 pt2 2334
f.close()

