#4-Reversing the Vowels
def check_vowel(s):
    if (s=="a" or s=="e" or s=="i" or s=="o" or s=="u"):
        return True
print("Enter the string:")    
string=str(input())
arr=[]
vow_arr=[]
for i in string:
    arr.append(i)
for i in string:
    if check_vowel(i):
        vow_arr.append(i)
for i in range(len(arr)):
    if check_vowel(arr[i]):
        arr[i]=vow_arr.pop()
print("".join(arr))
    