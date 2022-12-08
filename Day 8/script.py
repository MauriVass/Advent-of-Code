class Tree:
    def __init__(self, row, col, height):
        self.row = row
        self.col = col
        self.height = height
        if(height==9):
            val = True
        else:
            val = False
        self.visible_from_top = val
        self.visible_from_right = val
        self.visible_from_bottom = val
        self.visible_from_left = val

    def isVisible(self):
        visible = self.visible_from_top or self.visible_from_right or self.visible_from_bottom or self.visible_from_left
        return visible

# f = open('input.txt')
f = open('example.txt')
pt1 = False

forest = []

visible = 0
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
print(visible)
for r in range(1,row-1):
    for c in range(1,row-1):
        tree = forest[r][c]
        if(tree.isVisible()==False):
            #from top
            for top in range(0,r):
                h = forest[top][c].height
                if(h >= tree.height):
                    tree.visible_from_top = False
            if(tree.visible_from_top==False):
                tree.visible_from_top = True
                visible+=1

        if(tree.isVisible()==False):
            #from right
            for right in range(c+1,row):
                h = forest[r][right].height
                if(h >= tree.height):
                    tree.visible_from_right = True
            if(tree.visible_from_right==False):
                tree.visible_from_right = True
                visible+=1

        if(tree.isVisible()==False):
            #from bottom
            for bottom in range(r+1,row):
                h = forest[bottom][c].height
                if(h >= tree.height):
                    tree.visible_from_bottom = False
            if(tree.visible_from_bottom==False):
                tree.visible_from_bottom = True
                visible+=1

        if(tree.isVisible()==False):
            #from left
            for left in range(0,c):
                h = forest[r][bottom].height
                if(h >= tree.height):
                    tree.visible_from_left = False
            if(tree.visible_from_left==False):
                tree.visible_from_left = True
                visible+=1

print(visible)









