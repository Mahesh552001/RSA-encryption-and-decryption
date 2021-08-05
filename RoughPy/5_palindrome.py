
#5-Reverse and Palindrome
def obtain(num):
    rev_num=int("".join(reversed(str(num))))
    return rev_num+num
def check_palindrome(a):
    arr=[]
    for i in str(a):
        arr.append(i)
    for i in range(len(arr)//2):
        if arr.pop()!=arr.pop(0):
            return False
    else:
        return True
print("Enter a number:")
num=int(input())
b="True"
for i in range(5):
    a=obtain(num)
    num=a
    b=check_palindrome(a)
    if b:
        print(a)
        break
if b==False:
    print("No")




        



    



    
    
    

