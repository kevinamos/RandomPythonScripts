class BinaryTree(object):
    def __init__(self, rootObj):
        self.key=rootObj
        self.leftChild=None
        self.rightChild=None
    def insertLeft(self, newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            #create a binary tree using new node 2. attach current left to the created node. 3. assign the built node to current leftChild
            t=BinarTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t
    def insertRight(self, newNode):
        if self.rightChild==None:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t
        else:
            self.rightChild=BinaryTree(newNode)

            
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def setRoot(self, obj):
        self.key=obj

    def getRoot(self):
        return self.key


r=BinaryTree('a')
print(r.getRoot())
r.insertRight(4)
print(r.getRightChild().getRoot())
r.insertLeft('c')
print(r.getLeftChild().getRoot())

    


        
        
