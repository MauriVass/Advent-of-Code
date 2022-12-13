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

def checkElements(element1, element2):
    right_order = True
    counter = 0
    while counter < len(element1) or counter < len(element2):
        if (len(element1) > counter and len(element2) > counter):
            val1 = element1[counter]
            val2 = element2[counter]
            right_order = checkValues(val1, val2)
            if (right_order == False):
                break
        else:
            if (counter >= len(element1)):
                right_order = True
            else:
                right_order = False
            break
        counter += 1
    return right_order

def checkValues(val1, val2):
    right_order = True
    if(type(val1) == int and type(val2) == int): #both integers
        right_order = val1 <= val2 #check numerical values
    elif(type(val1)==int): #val2 is a list
        if(len(val2)>0):
            right_order = checkValues(val1, val2[0])
        else:
            return True
    elif(type(val2)==int): #same but this time val1 is a list
        if (len(val1) > 0):
            right_order = checkValues(val1[0], val2)
        else:
            return False
    else: #both lists
        right_order = checkElements(val1, val2)
    return right_order

f = open('input.txt')
# f = open('example.txt')

elements = {}

counter_line = 0
counter_groups = 1
result = 0
for line in f.readlines():
    line = line[1:-2] #remove initial [, final ] and final \n
    if(counter_line<2):
        elements[counter_line], _ = returnElement(line)
        counter_line += 1
    else:
        e1 = elements[0]
        e2 = elements[1]
        right_order = checkElements(e1, e2)
        if(right_order):
            result += counter_groups
            # print(elements[0])
            # print(elements[1])
            # print()
        counter_groups += 1
        counter_line = 0

f.close()

print(result)

