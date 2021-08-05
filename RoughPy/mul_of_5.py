# =============================================================================
# n=int(input())
# a=[]
# for i in range(0,n):
#     a.append(input())
# b=[]
# for i in range(0,n):
#     if (int(a[i])%5!=0):
#         b.append(a[i])
# print(b)
# =============================================================================
#find pieces of cutted circle
t=int(input())
for i in range(0,t):
    c=int(input())
    def cuts(c):
        if c==0:
            return(1)
        else:
            return(c+cuts(c-1))
    print(cuts(c))