                 #1-A

def set_union(a,b):
    ans=[i for i in a]
    for i in b:
        if i not in ans:
            ans.append(i)
    ans.sort()
    return ans
def set_intersection(a,b):
    ans=[]
    for i in a:
        if i in b:
            if i not in ans:
                ans.append(i)
    ans.sort()
    return ans
a_size=int(input())
b_size=int(input())
a=[]
b=[]
print("Enter set 1 elements:")
for i in range(a_size):
    a.append(int(input()))
print("Enter set 2 elements:")
for i in range(b_size):
    b.append(int(input()))
    
union=set_union(a,b)
intersection=set_intersection(a,b)
print("Union:",union)
print("Intersection",intersection)

                 #1-B
                 
def maximum(arr):
    maxi=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>maxi:
            maxi=arr[i]
    return maxi

def minimum(arr):
    mini=arr[0]
    for i in range(1,len(arr)):
        if arr[i]<mini:
            mini=arr[i]
    return mini
        
        
arr=list(map(int,input().split()))
print("Maximum:",maximum(arr))
print("Minimum:",minimum(arr))


                #1-C
                
def merge(arr1,arr2):
    for i in arr2:
        arr1.append(i)
    for i in range(len(arr1)-1):
        for j in range(len(arr1)-1-i):
            if arr1[j] > arr1[j+1] : 
                arr1[j], arr1[j+1] = arr1[j+1], arr1[j] 
    return arr1
            
        
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(merge(arr1,arr2))

