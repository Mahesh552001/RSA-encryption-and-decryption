                                    #infix to postfix
def preceding(s):
    if s=="-":return 1 
    elif s=="+":return 2
    elif s=="*":return 3
    elif s=="/":return 4
    elif s=="(":return 0
    
string=input()
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
