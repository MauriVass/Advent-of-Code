f = open('input.txt')

num_elves = 3
max_cals = []

cal = 0
for line in f.readlines():
    if (line == "\n"):
        if (len(max_cals) >= num_elves):
            for i in range(len(max_cals)):
                if (cal > max_cals[i]):
                    tmp = max_cals[i]
                    max_cals[i] = cal
                    cal = tmp
        else:
            max_cals.append(cal)
        cal = 0
    else:
        cal += int(line)

cal = 0
for i in max_cals:
    cal += i
print(cal)  # pt1 68787, pt2 198041
