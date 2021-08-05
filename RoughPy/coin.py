                                             #coins

def compute_min_num_of_coins(n,coins):
    arr=[i for i in range(n+1)]
    for coin in coins:
        for i in range(coin,n+1):
            arr[i]=min(arr[i],(arr[i-coin]+1)) 
    print(arr[-1])

def compute_num_of_ways(n,coins):
    arr=[1]+[0]*n
    for coin in coins:
        for i in range(coin,n+1):
            arr[i]=arr[i]+arr[i-coin]
    print(arr[-1])
    
n=int(input())
coins=list(map(int,input().split()))
compute_min_num_of_coins(n,coins)
compute_num_of_ways(n,coins)