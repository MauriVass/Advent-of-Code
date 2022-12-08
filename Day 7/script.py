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
        s = current_size + children_size
        if (s < 100000):
            sizes[self.name] = s
        return s

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
        if(file[0] == 'dir'):
            _ = 1 #do nothing
        else:
            current_directory.addFile(file[-1], int(file[0]))

root.calculateSize()
size = 0
for s in sizes.values():
    size+=s
print(size) #pt1 1611443
f.close()

