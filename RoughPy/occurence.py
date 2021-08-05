



# finding the binarys consecutive 1
n = int(input())
temp=list((bin(n)))
binary=temp[2:]
count=0
result=0
for i in range(len(binary)):
    if binary[i]=="0":
        count=0
    else:
        count+=1
        result=max(result,count)
print(result)





#capitalize each word in string                       
x=input()
l=[]
l=x.split(" ")
for i in range(len(l)):
    l[i]=l[i].capitalize()
x=" ".join(l)
print(x)


#lst3 = [value for value in lst1 if value in lst2] 


#textwrap
#import textwrap
#wrapper=textwrap.TextWrapper(width=)
#ans=wrapper.fill(text=) return fill string separated by new lines
#ans=wrapper.wrap(text=) returns a list


#set(str) will return set
#list(str)
#list("abcd")==["a","b","c","d"]


# Function to remove all duplicates from string  
# and keep the order of characters same 
###
#from collections import OrderedDict
#"".join(OrderedDict.fromkeys(str))  
  