

                         #DICTIONARY
#Given the names and grades for each student in a class of  students, store them
#in a nested list and print the name(s) of any student(s) having the second lowest grade.

#Note: If there are multiple students with the second lowest grade, order their names 
#alphabetically and print each name on a new line.

n=int(input())
stu={}
for i in range(n):
    name=input()
    mark=float(input())
    stu[name]=mark
m=[*stu.values()]
m=set(m)
m=list(m)
m.sort()
sm=m[1]
result=[]
for key in stu:
    if stu[key]==sm:
        result.append(key)
result.sort()
for item in result:
    print(item)
#[*dict] return a list of keys which means it iterrates through the keys [*dict.keys()]
#[*dict.values()]
    
    
    

#printing the ph book as dict
n=int(input())
ph_book={}
for i in range(n):
    a,b=input().split()
    ph_book[a]=b
try:
    while True:
        query=input()
        if query=="quit":
            break
        try:
            print("{}={}".format(query,ph_book[query]))
        except:
            print("Not found")
except EOFError:
    pass





#The first line contains , the number of shoes.
#The second line contains the space separated list of all the shoe sizes in the shop.
#The third line contains , the number of customers.
#The next  lines contain the space separated values of the shoe size desired by the customer and ,
#the price of the shoe.  print(total price earned)
from collections import Counter 
#A counter is a container that stores elements as dictionary keys,
      #and their counts are stored as dictionary values.
x=int(input())
sizes=list(map(int,input().split()))
n=int(input())
l=Counter(sizes)
result=0
for i in range(n):
    size,p=map(int,input().split())
    if size in l.keys():
        l[size]=l[size]-1
        if l[size]==0:
            del l[size]
        result+=p
print(result)




#refer hr=collections.OrderedDict 
from collections import OrderedDict
n=int(input())
d=OrderedDict()
for i in range(n):
    *a,p=input().split()
    b=" ".join(a)
    p=int(p)
    if b in d:
        d[b]+=p
    else:
        d[b]=p
for x,y in d.items():
    print(x,y)
    
    
#refer hr=word order
from collections import OrderedDict
n=int(input())
d=OrderedDict()
for i in range(n):
    word=input()
    if word in d:
        d[word]+=1
    else:
        d[word]=1
print(len([*d]))
v=[*d.values()]
for i in range(len(v)):
    print(v[i],end=' ')






                                
                            #sets
#one list l ,two sets A and B , for each element in a belongs to l add 1 , and in b sub 1
n,m=list(map(int, input().split()))
l=list(map(int, input().split()))
a=set(map(int, input().split()))
b=set(map(int, input().split()))
res=0
for x in l:
    if x in a:
        res+=1
    elif x in b:
        res-=1
print(res)


#refer hr=grading students
#refer hr=kangaroo
#refer hr=sorting:comparator
#refer hr=pairs
#refer hr=drawing book
#refer hr=append and delete
#refer hr=encryption
#refer hr=electronic shop
#refer hr=designer door mat
#refer hr=alphabet rangoli
#refer hr=counting valley
#refer hr=ACM ICPC Team
#refer hr=queues and stacks in OOPS
#refer hr=Morgan and a String
#refer hr=maximum subarray #also leetcode


