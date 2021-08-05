import math
class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def r_area(self):
        ar=self.l*self.b
        return ar
class circle:
    def __init__(self,r):
        self.r=r
    def c_area(self):
        ac=self.r*self.r*math.Pi
        return ac
q=int(input())
for i in range (0,q):
    x,y,z=input().split()
    if z==0:
        a1=circle(y)
        ans=a1.c_area()
        print(ans)
    else:
        b1=rectangle(y,z)
        sol=b1.r_area()
        print(sol)

        
import math
class shape:
    def __init__(self,name,l,b=None):
        if b!=None:
            self.name=name
            self.l=l
            self.b=b
        else:
            self.name=name
            self.l=l
            
    def area(self):
        if self.name=="rectange":
            ar=self.l*self.b
            return ar
            
        else:
            ac=self.l*self.l*math.pi
            return ac

y1=shape("rectange",2,4)
y2=shape("circle",2)
ans1=y1.area()
ans2=y2.area()
print(ans1,"\n",ans2)
            
    





fname = input("Enter file name: ")
fh = open(fname)
lst = list()
a=[]
b=[]
for line in fh:
    a=line.split()
    for i in range(0,len(a)):
        b.append(a[i])
b.sort()
c=set(b)
print(list(c))
#The program should build a list of words. 
#For each word on each line check to see if the word is already in the list 
#and if not append it to the list. When the program completes, sort and 
#print the resulting words in alphabetical order.








fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if line.startswith('From'):
        if not line.startswith('From:'):
            a=line.split()
            print(a[1])
            count+=1

print("There were", count, "lines in the file with From as the first word")










#dict()
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
b=[]
for line in handle:
    if line.startswith('From'):
        if not line.startswith('From:'):
            a=line.split()
            b.append(a[1])
            
        
a=dict()
for word in b:
    if word in a:
        a[word]=a[word]+1
    else:
        a[word]=1
b=a.values()
i=b.index(max(b))
c=a.keys()
print(c[i],max(b))





#time
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
a=[]
x=[]
for line in handle:
    if line.startswith('From'):
        if not line.startswith('From:'):
            a=line.split()
            b=a[5]
            c=b[:2]
            x.append(c)
x.sort()
z=dict()
for i in x:
    if i in z:
        z[i]+=1
    else:
        z[i]=1
k=z.keys()
v=z.values()
for i in range(0,len(v)):
    print(k[i],v[i])
    
    
    
    
    
                                   