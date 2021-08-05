                           #2-A

#implementation of stack using array
class stack:
    def __init__(self,maxsize):
        self.stack=list()
        self.maxsize=maxsize
        self.top=-1
    def push(self,data):
        if self.isFull():
            return ("Stack is Full")
        self.stack.append(data)
        self.top+=1
        return ("Done")
    def pop(self):
        if self.isEmpty():
            return ("Stack is Empty")
        item=self.stack.pop()
        self.top-=1
        return item
    def peep(self):
        if self.isEmpty():
            return ("Stack is empty")
        return self.stack[self.top]
    def isEmpty(self):
        if self.top==-1:
            return True
        return False
    def isFull(self):
        if self.top+1==self.maxsize:
            return True
        return False
    def size(self):
        return self.top+1
s=stack(3)

                             #2-B

#infix to postfix
def preceding(s):
    if s=="-":return 1 
    elif s=="+":return 2
    elif s=="*":return 3
    elif s=="/":return 4
    elif s=="(":return 0 
def check_for_balancing(string):
    stack=[]
    dictionary={"{":"}","[":"]","(":")"}
    for i in string:
        if i=="(" or i=="{" or i=="[":
            stack.append(i)
        elif i==")" or i=="}" or i=="]":
            if len(stack)>0 and dictionary[stack[len(stack)-1]]==i:
                stack.pop()
            else:
                return "NOT BALANCED"        
    if len(stack)!=0:
        return "NOT BALANCED"
    else:
        return "BALANCED"
string=input()
if check_for_balancing(string)=="NOT BALANCED":
    print("The string is not balanced")
else:
    operators=["+","-","*","/","(",")"]
    array=[] 
    stack=[] 
    for i in string:
        if i not in operators:
            array.append(i) 
        else:
            if len(stack)==0:
                stack.append(i)
            elif i==")":
                while stack[-1]!="(":
                    array.append(stack.pop())
                stack.pop()
            elif preceding(i)>preceding(stack[-1]):
                stack.append(i)
            else:
                if i=="(":
                    stack.append(i)
                else:
                    array.append(stack.pop())
                    stack.append(i)          
    for i in reversed(stack):
        array.append(i)
    print("".join(array))


#String reversal
string=input()
stack=[]
for i in string:
    stack.append(i)
for i in string:
    print(stack.pop(),end="")   
    
#palindrome checking
def isPalindrome(string):
    stack=[]
    for i in string:
        stack.append(i)
    i=0
    for _ in stack:
        ch=stack.pop()
        if ch!=string[i]:
            return False
        i+=1
    return True
string=input()
print(isPalindrome(string))
    

