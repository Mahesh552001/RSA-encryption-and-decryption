n=int(input("enter no. elements"))
y=[]
for i in range(0,n):
    y.append(input("enter values"))
z=[]
for i in range(len(y)-1,-1,-1):
    z.append(y[i])
x=[]
for i in range(0,n):
    x.append(int(y[i])+int(z[i]))
print(x)



    