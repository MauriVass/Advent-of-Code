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
        sizes = []
        current_size = 0
        children_size = 0
        for s in self.files.values():
            current_size += s
        for c in self.children:
            sublist = c.calculateSize()
            for s in sublist:
                children_size += s
                if(children_size<100000):
                    sizes.append(s)
        s = current_size + children_size
        v = 0class File:
    def __init__(self, name: str, fileSize: int):
        self.name = name
        self.size = fileSize

    def __str__(self) -> str:
        return f"{self.name} - {self.size}"


class Directory:
    subdiretories: []
    files: [File]

    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self.subdiretories = []
        self.files = []

    def size(self) -> int:
        total = 0
        for sub in self.subdiretories:
            total += sub.size()

        for file in self.files:
            total += file.size

        return total

    def addSub(self, other):
        self.subdiretories.append(other)

    def addFile(self, file: File):
        self.files.append(file)

    def __str__(self) -> str:
        rv = f"Dir: {self.name} - {self.size()}\n"
        for file in self.files:
            rv += f"\t File: {file}\n"

        for sub in self.subdiretories:
            rv += f"\t {sub}\n"

        return rv


def checkAllowedDirs(currDir: Directory):
    for sub in currDir.subdiretories:
        if sub.size() < 100000:
            allowedDirs.append(sub)

        checkAllowedDirs(sub)


def checkDeletable(currDir: Directory):
    for sub in currDir.subdiretories:
        if sub.size() >= SPACENEEDEDTOBECLREAED:
            possibleDeletes.append(sub)
        checkDeletable(sub)


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        raw = [line.replace("\n", "") for line in f.readlines()]

    currentlyLS = False

    fileSystem = Directory("ROOT", "")
    currentDir: Directory = fileSystem

    for line in raw:
        if line.startswith("$"):
            if "cd" in line:
                where = line.split(" ")[2]
                if where == "..":
                    currentDir = currentDir.parent
                else:
                    createdDir = Directory(where, currentDir)
                    currentDir.addSub(createdDir)
                    currentDir = createdDir
        else:
            size, currentName = line.split(" ")
            if size.isnumeric():
                currentDir.addFile(File(currentName, int(size)))

    allowedDirs = []
    checkAllowedDirs(fileSystem)
    print(f"Solution 1: {sum([allowedDir.size() for allowedDir in allowedDirs])}")

    possibleDeletes = []

    TOTALSPACE = 70000000
    SPACEREQUIRED = 30000000
    USEDSPACE = fileSystem.size()
    SPACENEEDEDTOBECLREAED = SPACEREQUIRED - (TOTALSPACE - USEDSPACE)

    checkDeletable(fileSystem)

    print(f"Solution 2: {min([possibleDelete.size() for possibleDelete in possibleDeletes])}")

        # if(self.parent):
        #     print(self.parent.name, self.name, s)
        # else:
        #     print(self.name, s)
        if(s < 100000):
            v = current_size + children_size
            sizes.append(v)
        else:
            if(current_size<children_size):
                if(current_size < 100000):
                    v = current_size
                else:
                    v = 0
            else:
                if (children_size < 100000):
                    v = children_size
                else:
                    v = 0
        # print(sizes)
        # print(sizes)
        return sizes


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
            # print(file, line)
            current_directory.addFile(file[-1], int(file[0]))

print(root.calculateSize()) #pt1 1920 pt2 2334
f.close()

