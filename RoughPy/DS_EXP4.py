                       #implementation of linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def Insert_at_begin(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
        
    def Insert_after(self,after,data):
        temp=self.head
        newnode=Node(data)
        pre_node=None
        while(temp):
            if temp.data==after:
                pre_node=temp
                break
            temp=temp.next
        if pre_node==None:
            return "Node not found"
        else:
            newnode.next=pre_node.next
            pre_node.next=newnode
            
    def Insert_at_end(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
            
    def Delete(self,data):
        check=False
        temp=self.head
        if temp.data==data:
            check=True
            self.head=self.head.next
        else:
            while(temp.next!=None):
                if temp.next.data==data:
                    check=True
                    temp.next=temp.next.next
                    break
                temp=temp.next
        if check==False:
            return "Node not found"
    
    def Search(self,data):
        check=False
        temp=self.head
        while(temp):
            if temp.data==data:
                check=True
                break
            temp=temp.next
        if check==True:
            return "Node found"
        return "Node not Found"
    
    def Count(self):
        count=0
        temp=self.head
        while(temp):
            count+=1
            temp=temp.next
        return count
        
    def Sort(self):
        temp=self.head
        arr=[]
        while(temp):
            arr.append(temp.data)
            temp=temp.next
        arr.sort()
        i=0
        temp=self.head
        while(temp):
            temp.data=arr[i]
            temp=temp.next
            i+=1
        self.PrintList()
        
    def Reverse(self):
          prev=None
          current=self.head
          while (current is not None):
              next=current.next
              current.next=prev
              prev=current
              current=next
          self.head=prev
          self.PrintList()
          
    def PrintList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
    
    
            
llist=LinkedList()





