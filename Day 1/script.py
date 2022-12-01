f = open('input.txt')

max_cal = 0

cal = 0
for i in f.readlines():
	if(i=="\n"):
		if(cal>max_cal):
			max_cal=cal
		cal = 0
	else:
		cal+=int(i)
print(max_cal)