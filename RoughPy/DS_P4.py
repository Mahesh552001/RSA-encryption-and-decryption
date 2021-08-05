class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.head2=None
        
    def Insert1(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
            
    def Insert2(self,data):
        newnode=Node(data)
        if self.head2==None:
            self.head2=newnode
        else:
            temp=self.head2
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
        
    def Delete2(self,data):
        check=False
        temp=self.head2
        if temp.data==data:
            check=True
            self.head2=self.head2.next
        else:
            while(temp.next!=None):
                if temp.next.data==data:
                    check=True
                    temp.next=temp.next.next
                    break
                temp=temp.next
        if check==False:
            return "Node not found"
    
    
    def Find(self,data):
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
    
    def Find2(self,data):
        check=False
        temp=self.head2
        while(temp):
            if temp.data==data:
                check=True
                break
            temp=temp.next
        if check==True:
            return "Node found"
        return "Node not Found"
     
    def PrintList1(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
            
    def PrintList2(self):
        temp=self.head2
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
    
    def u(self):
        arr1=[]
        arr2=[]
        temp=self.head
        while(temp):
            arr1.append(temp.data)
            temp=temp.next
        temp2=self.head2
        while(temp2):
            arr2.append(temp2.data)
            temp2=temp2.next
        ans=[i for i in arr1]
        ans=list(set(ans))
        for i in arr2:
            if i not in ans:
                ans.append(i)
                ans.sort()
        print(ans)
    
    def i(self):
        arr1=[]
        arr2=[]
        temp=self.head
        while(temp):
            arr1.append(temp.data)
            temp=temp.next
        temp2=self.head2
        while(temp2):
            arr2.append(temp2.data)
            temp2=temp2.next
        ans=[]
        for i in arr1:
            if i in arr2:
                if i not in ans:
                    ans.append(i) 
        ans.sort()
        print(ans)
        

        