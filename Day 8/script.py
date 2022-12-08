class Tree:
    def __init__(self, row, col, height):
        self.row = row
        self.col = col
        self.height = height
        val = 1
        self.visible_from_top = val
        self.visible_from_right = val
        self.visible_from_bottom = val
        self.visible_from_left = val

    def isVisible(self):
        visible = self.visible_from_top==0 or \
                  self.visible_from_right==0 or \
                  self.visible_from_bottom==0 or \
                  self.visible_from_left==0
        return visible

f = open('input.txt')
# f = open('example.txt')
pt1 = False

forest = []

row = 0
for line in f.readlines():
    tmp = []
    col = 0
    for c,n in enumerate(line[:-1]):
        tree = Tree(row, c, int(n))
        tmp.append(tree)
    forest.append(tmp)
    row+=1
f.close()

visible = 4 * (row-1)
for r in range(1,row-1):
    for c in range(1,row-1):
        tree = forest[r][c]
        if(tree.isVisible()==False):
            #from top
            for top in range(0,r):
                h = forest[top][c].height
                if(h >= tree.height):
                    tree.visible_from_top += 1
            if(tree.visible_from_top==1):
                tree.visible_from_top = 0
                visible+=1

        if(tree.isVisible()==False):
            #from right
            for right in range(c+1,row):
                h = forest[r][right].height
                if(h >= tree.height):
                    tree.visible_from_right += 1
            if (tree.visible_from_right == 1):
                tree.visible_from_right = 0
                visible += 1

        if(tree.isVisible()==False):
            #from bottom
            for bottom in range(r+1,row):
                h = forest[bottom][c].height
                if(h >= tree.height):
                    tree.visible_from_bottom += 1
            if (tree.visible_from_bottom == 1):
                tree.visible_from_bottom = 0
                visible += 1

        if(tree.isVisible()==False):
            #from left
            for left in range(0,c):
                h = forest[r][left].height
                if(h >= tree.height):
                    tree.visible_from_left += 1
            if (tree.visible_from_left == 1):
                tree.visible_from_left = 0
                visible += 1
print(visible) #pt1 1711









