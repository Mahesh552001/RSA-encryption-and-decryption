n=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
result=[]
for i in range(n):
    target=arr[i]
    for j in range(i+1,n):
        element=target-arr[j]
        if element in arr[j+1:]:
            result.append((arr[j],element,"gives:"+str(target)))
if len(result)!=0:
    for i in result:
        print(i)
else:
    print("NONE (Not Possible)")
    