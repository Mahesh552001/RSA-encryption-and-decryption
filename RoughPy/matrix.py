

import numpy as npy
a,b=map(int,input().split())
count=1
m = []
for i in range(a):
    l = []
    for j in range(b):
        l.append(count)
        count+=1
    m.append(l)
y=npy.array(m)
print(y)
 
for i in range(a):
    for j in range(b):
        if (j==b-1):
            print(m[i][j],end="")
        else:
            print(m[i][j],end=" ")
    print()







n,m=map(int,input().split())
a=[]
for i in range(0,n):
    b=list(map(int,input().split()))
    a.append(b)
c=[]
x=0
for i in range (0,m):
    d=[]
    for j in range(0,n):
        d.append(a[j][x])
    x+=1
    c.append(d)
for i in range(m):
    for j in range(n):
        if (j==n-1):
            print(c[i][j],end="")
        else:
            print(c[i][j],end=" ")
    print()

    
    
    
    





#get imput in a same line as name of student and their mark ,,,,, 
#then it returns avg mark of the student which we asked(query name)
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split() #importantttttttttt
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a=[]
    a=student_marks[query_name]
    temp=0
    for num in a:
        temp=temp+num
    print("{:.2f}".format(temp/3))
    




sentence = input("Enter a sentence :") #importantttt
print(" ".join(reversed(sentence.split())))
#something.sort(reverse=True)


