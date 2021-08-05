#itertools
import itertools  
    
# for in loop  
for i in itertools.count(5, 5):  
    if i == 35:  
        break
    else:  
        print(i, end =" ") 
        
        
count = 0
    
# for in loop  
for i in itertools.cycle('AB'):  
    if count > 7:  
        break
    else:  
        print(i, end = " ")  
        count += 1
        
l = ['Geeks', 'for', 'Geeks']  
    
# defining iterator  
iterators = itertools.cycle(l)  
    
# for in loop  
for i in range(6):  
        
    # Using next function  
    print(next(iterators), end = " ")  

print ("Printing the numbers repeatedly : ")   
print (list(itertools.repeat(25, 4))) 

print ("All the permutations of the given string is:")   
print (list(itertools.permutations('AB')))  
print()  





# Enter your code here. Read input from STDIN. Print output to STDOUT
#printing combinations of a word for given range of index in lexiographic order
from itertools import combinations
a,b=input().split()
b=int(b)
for i in range(1,b+1):
    t=list(combinations(a,i))
    for i in range(len(t)):
        y=list(t[i])
        y.sort()
        t[i]=y
    t.sort()
    for i in range(len(t)):
        x=t[i]
        for item in x:
            print(item,end='')
        print(' ')
