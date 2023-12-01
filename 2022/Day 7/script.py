sizes = {}
class Node():
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        if(parent is not None):
            parent.addNode(self)
        self.children = []
        self.files = {}

    def addNode(self, node):
        self.children.append(node)
    def addFile(self, name, size):
        if(name not in self.files.keys()):
            self.files[name] = size
    def returnParent(self):
        return self.parent
    def returnChildren(self, name):
        for c in self.children:
            if(name == c.name):
                return c
        c = Node(name, self)
        return c

    def calculateSize(self):
        current_size = 0
        children_size = 0
        for s in self.files.values():
            current_size += s
        for c in self.children:
            s = c.calculateSize()
            children_size += s
        total_size = current_size + children_size
        name = self.parent.name+self.name if self.parent != None else self.name
        sizes[name] = total_size
        return total_size

f = open('input.txt')
# f = open('example.txt')
pt1 = False

root = Node('/')

current_directory = root
for line in f.readlines():
    line = line[:-1]
    if(line[0]=='$'):
        command = line.split(' ')
        if(len(command)>2): # cd
            directory = command[-1]
            if(directory=='..'):
                current_directory = current_directory.returnParent()
            elif(directory=='/'):
                current_directory = root
            else:
                current_directory = current_directory.returnChildren(directory)

        # else: # ls. No need to do anything actually
    else:
        file = line.split(' ')
        if(file[0] != 'dir'):
            current_directory.addFile(file[-1], int(file[0]))

root.calculateSize()
size = 0
for s in sizes.values():
    if (s < 100000):
        size += s
print(size) #pt1 1611443
f.close()

available_space = 70000000
required_space = 30000000
delete_space = required_space - (available_space - sizes['/'])
print('Space to be cleared:', delete_space)
min_deletion = available_space #inf

for v in sizes.values():
    if(v > delete_space and v < min_deletion):
        min_deletion = v
print(min_deletion) #pt2 2086088



