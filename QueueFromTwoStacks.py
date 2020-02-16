class QueueFromTwoStacks():
    def __init__(self):
        self.instack=[]
        self.outstack=[]
    def Enqueue(self, element):
        self.instack.append(element)
        return self.instack
    def Dequeque(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        self.outstack.pop()
        return self.outstack
        

ob1=QueueFromTwoStacks()

ob1.Enqueue(1)
ob1.Enqueue(2)
ob1.Enqueue(4) 


print (ob1.Enqueue(5))

print(ob1.Dequeque())
