#2-Zig Zag
import numpy as npy
n=int(input())
matrix=[]
print("Enter the rows of a matrix")
for i in range(n):
    rows=list(map(int,input().split()))
    matrix.append(rows)
y=npy.array(matrix) 
arr=[]
for i in range(-n+1,n):
    arr.append(y[::-1,:].diagonal(i))
l=[]
for i in arr:
    l.append(i.tolist())
for i in range(len(l)):
    if i%2!=0:
        l[i].reverse()
answer=[]
for i in l:
    for j in i:
        answer.append(j)
answer.reverse()
for i in answer:
    print(i,end=" ")