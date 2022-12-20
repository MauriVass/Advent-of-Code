f = open('input.txt')
# f = open('example.txt')

initial_coordinates = []
decrypted_coordinates = []

for i,line in enumerate(f.readlines()):
    v = int(line[:-1])
    initial_coordinates.append((i, v))
    decrypted_coordinates.append((i, v))
f.close()

length_coords = len(initial_coordinates)

print(initial_coordinates)
for i,v in initial_coordinates:
    ind = decrypted_coordinates.index((i,v))

    decrypted_coordinates.pop(ind)
    new_ind = (ind + v) % (length_coords - 1)
    decrypted_coordinates.insert(new_ind, (i,v))

decrypted_coordinates = [i[1] for i in decrypted_coordinates]
ind_0 = decrypted_coordinates.index(0)
result = decrypted_coordinates[(ind_0 + 1000) % length_coords] + \
        decrypted_coordinates[(ind_0 + 2000) % length_coords] + \
        decrypted_coordinates[(ind_0 + 3000) % length_coords]

print(result) #pt1 13883

