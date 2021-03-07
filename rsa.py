                                             #RSA
#function to calculate gcd by euclidean algorithm
def gcd(x, y): 
   while(y): 
       x, y = y, x % y 
   return x 

operation=int(input("Encryption-1 or Decryption-2 "))
p=int(input("p "))
q=int(input("q "))
message=int(input("message "))

n=p*q
m=(p-1)*(q-1)

#finding public key e
i=2
while(True):
    if gcd(i,m)==1:
        e=i
        break
    i=i+1
#finding private key d
j=1
while(True):
    if (e*j)%m==1:
        d=j
        break
    j=j+1

if operation==1: #(encrption)
    ciphertext=(message**e)%n
    print("\nciphertext =",ciphertext)
else: #(decryption)
    plaintext=(message**d)%n
    print("\nplaintext =",plaintext)
    
    