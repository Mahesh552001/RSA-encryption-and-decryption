class Bst:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
        
    def Insert(self, data):
        if self.data==None:
            self.data=data
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.Insert(data)
            else:
                self.left= Bst(data)
        else:
            if self.right:
                self.right.Insert(data)
            else:
                self.right = Bst(data)
                
    def Find_Node(self,data):
        if self.data == data:
            return True

        if data < self.data:
            if self.left:
                return self.left.Find_Node(data)
            else:
                return False
        
        if data > self.data:
            if self.right:
                return self.right.Find_Node(data)
            else:
                return False
            
    def In_Order(self):
        if self.left:
            self.left.In_Order()
        print (self.data)
        if self.right:
            self.right.In_Order()
            
    def Post_Order(self):
        if self.left:
            self.left.Post_Order()
        if self.right:
            self.right.Post_Order()
        print (self.data)
    
    def Pre_Order(self):
        print (self.data)
        if self.left:
            self.left.Pre_Order()
        if self.right:
            self.right.Pre_Order()
            
    def Find_Max(self):
        if self.right is None:
            return self.data
        return self.right.Find_Max()
    
    def Find_Min(self):
        if self.left is None:
            return self.data
        return self.left.Find_Min()
    
    def Delete(self,data):
        if self.data==None:
            return("The tree is empty")
        if data<self.data:
            self.left.Delete(data)
        elif data>self.data:
            self.right.Delete(data) 
        else:
            if self.right==None and self.left==None:
                self.data = None
            elif self.left is None:
                self.data=self.right.data
                self.right=None
            elif self.right is None:
                self.data=self.left.data
                self.left=None
            else:
                temp=self.right.Find_Min()
                self.data=temp
                self.right.Delete(temp)     
tree=Bst()



#pre from post and in
postIndex = 0
def fillPre(In, post, inStrt, inEnd, s, hm):
	global postIndex
	if(inStrt > inEnd):
		return
	val = post[postIndex]
	inIndex = hm[val]
	postIndex -= 1
	fillPre(In, post, inIndex + 1, inEnd, s, hm)
	fillPre(In, post, inStrt, inIndex - 1, s, hm)
	s.append(val)
def printPreMain(In, post):
	global postIndex
	Len = len(In)
	postIndex = Len - 1
	s = []
	hm = {}
	for i in range(len(In)):
		hm[In[i]] = i
	fillPre(In, post, 0, Len - 1, s, hm)
	while(len(s) > 0):
		print(s.pop(), end = " ")
In = list(map(str,input().split()))
post = list(map(str,input().split()))
printPreMain(In, post)



#post from pre and in
def printPost(inn, pre, inStrt, inEnd):
	global preIndex, hm
	if (inStrt > inEnd):
		return
	inIndex = hm[pre[preIndex]]
	preIndex += 1
	printPost(inn, pre, inStrt, inIndex - 1)
	printPost(inn, pre, inIndex + 1, inEnd)
	print(inn[inIndex], end = " ")
def printPostMain(inn, pre, n):

	for i in range(n):
		hm[inn[i]] = i

	printPost(inn, pre, 0, n - 1)
if __name__ == '__main__':
	hm = {}
	preIndex = 0
	inn = list(map(str,input().split()))
	pre = list(map(str,input().split()))
	n = len(pre)
	printPostMain(inn, pre, n)


        