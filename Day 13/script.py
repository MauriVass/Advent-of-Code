def returnElement(line):
    elems = []
    counter = 0
    while counter<len(line):
        l = line[counter]
        if (l == '['):
            a, c = returnElement(line[counter+1:])
            counter += c+1
            elems.append(a)
        elif(l == ']'):
            break
        elif(l not in [' ', ',']):
            num = ''
            ll = '-1'
            c = 0
            while True:
                if(counter+c < len(line)):
                    ll = line[counter+c]
                    if(ll not in ['[', ']', ',', ' ']):
                        num += ll
                    else:
                        break
                    c+=1
                else:
                    break
            elems.append(int(num))
        counter+=1
    return elems, counter

def checkValues(val1, val2):
    if(type(val1) == int and type(val2) == int): #both integers
        if(val1 < val2): #check numerical values
            return 1
        if(val1 > val2):
            return -1
        return 0

    elif(type(val1)==int): #val2 is a list
        return checkValues([val1], val2)
    elif(type(val2)==int): #same but this time val1 is a list
        return checkValues(val1, [val2])
    else: #both lists
        counter = 0
        while counter < len(val1) and counter < len(val2):
            right_order = checkValues(val1[counter], val2[counter])
            if (right_order != 0):
                return right_order
            counter += 1
        if (len(val1) < len(val2)):
            return 1
        elif (len(val1) > len(val2)):
            return -1
    return 0

f = open('input.txt')
# f = open('example.txt')

elements = {}

counter_line = 0
counter_groups = 1
result = 0
all_elements = []
for line in f.readlines()+['[.]\n']:
    line = line[1:-2] #remove initial [, final ] and final \n
    if(counter_line<2):
        ele, _ = returnElement(line)
        elements[counter_line] = ele
        all_elements.append(ele)
        counter_line += 1
    else:
        e1 = elements[0]
        e2 = elements[1]
        right_order = checkValues(e1, e2)
        if(right_order==1):
            result += counter_groups
        counter_groups += 1
        counter_line = 0

f.close()

print(result) #pt1 5825

# Python program for implementation of Bubble Sort


def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if checkValues(arr[j], arr[j+1]) == -1:
                arr[j], arr[j+1] = arr[j+1], arr[j]

all_elements.append([[2]])
all_elements.append([[6]])

bubbleSort(all_elements)

ind_of2 = all_elements.index([[2]]) + 1
ind_of6 = all_elements.index([[6]]) + 1
print(ind_of2 * ind_of6)


