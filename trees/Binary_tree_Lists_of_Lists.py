def BinaryTree(r):
    """ first element=root, second-left branch, third=right branch"""
    return [r, [], []]

def insertLeft(root, newBranch):
    t=root.pop(1) #pop out first item
    if len(t)>1:
        root.insert(1,[newBranch, t, []] )
    else:
        root.insert(1, [newBranch, [], []])
    return root
def insertRight(root, newBranch):
    t=root.pop(2) #pop out first item
    if len(t)>1:
      root.insert(2,[newBranch,[], t ])
    else:
        root.insert(2, [newBranch, [], []])
    return root

def getRootVal(root, val):
    return root[0]

def setRootVal(root, newval):
    root[0]=newval

def getLeftChild(root, newval):
    return root[1]

def getRightChild(root, newval):
    return root[2]

root=BinaryTree(3)
print(root)
insertLeft(root, 4)
print(root)
insertLeft(root, 5)
print(root)
insertLeft(root, 6)
print(root)
insertLeft(root, 7)
print(root)

