n=input("enter binary no.s")
m=[]
for i in n:
    m.append(int(i))
print(m)
count_zero=0
count_one=0
for j in range(len(m)):
    if(int(m[j])==0):
        count_zero=count_zero+1
    else:
        count_one=count_one+1
if(count_zero==1 or count_one==1):
    print("true")
else:
    print("false")

