
def check(string):
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
print(check(string))

    
        
