
class Queue:
    def __init__(self,size):
        self.queue=list()
        self.size=size
        self.front=-1
        self.rear=-1
    def enQueue(self,data):
        if self.isFull():
            return ("Queue is Full")
        self.queue.append(data)
        self.rear+=1
        return ("Done")
    def deQueue(self):
        if self.isEmpty():
            return ("Queue is Empty")
        item=self.queue.pop(0)
        self.front+=1
        return item
    def isFull(self):
        if self.rear==self.size-1:
            return True
        return False
    def isEmpty(self):
        if self.front==self.rear:
            return True
        return False
q=Queue(3)


from numpy import ndarray
class circularQueue:
    def __init__(self,size):
        self.queue=ndarray(size,int)
        self.size=size
        self.front=-1
        self.rear=-1
    def enQueue(self,data):
        if self.isFull():
            return ("Queue is Full")
        self.rear=(self.rear+1)%self.size
        self.queue[self.rear]=data
        return ("Done")
    def deQueue(self):
        if self.isEmpty():
            return ("Queue is Empty")
        self.front=(self.front+1)%self.size
        item=self.queue[self.front]
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        return item
    def isFull(self):
        if ((self.front==-1 and self.rear==(self.size-1)) or (self.front!=-1 and self.front==self.rear)): 
            return True
        return False
    def isEmpty(self):
        if (self.front==-1 and self.rear==-1):
            return True
        return False
cq=circularQueue(3)


    
            
    
    