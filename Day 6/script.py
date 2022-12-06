f = open('input.txt')
# f = open('example.txt')
pt1 = True

start_of_packet_marker_index = 0
characters = []
length_starter = 4
for index, character in enumerate(f.read()):
    if(index>=length_starter):
        characters.pop(0)
    characters.append(character)
    if(index>2 and len(set(characters))==length_starter):
        start_of_packet_marker_index = index+1
        break

print(start_of_packet_marker_index) #pt1 1920
f.close()

