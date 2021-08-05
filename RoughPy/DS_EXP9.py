fh=open("sorting.txt")
arr=[]
for line in fh:
    temp=list(map(int,line.split()))
    arr.extend(temp)

import time
#BUBBLE SORT
print("\nBUBBLE SORT")
start =time.time()
for i in range(len(arr)-1):
    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
end=time.time()
print(arr)
print(end-start)

#INSERTION SORT
print("\nINSERTION SORT")
arr=list(map(int,input().split()))
for i in range(1,len(arr)):
    temp=arr[i]
    j=i-1
    while j>=0 and temp<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=temp
    print(arr)
print("final:",arr)

#MERGE SORT
print("\nMERGE SORT")
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
            
start =time.time()
print(mergeSort(arr))
end=time.time()
print(end-start)


#SHELL SORT
print("\nSHELL SORT")
def shellSort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
  
n = len(arr)
arr=list(map(int,input().split()))
print(shellSort(arr))

#QUICK SORT
print("\nQUICK SORT")
def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]
    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1
        if(start < end):
            array[start], array[end] = array[end], array[start]
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end

def quick_sort(start, end, array):
    if (start < end):
        p = partition(start, end, array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
        
arr=list(map(int,input().split()))
quick_sort(0, len(arr)-1, arr)
print(arr)




    
    