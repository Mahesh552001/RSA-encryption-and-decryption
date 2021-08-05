#1-M Pattern
rows=int(input())
cols=(rows*4)-3
matrix=[]

for i in range(rows):
    matrix.append([" " for i in range(cols)])
    
for i in range(1,rows+1):
    matrix[rows-i][i-1]="*"
for i in range(0,rows):
    matrix[i][rows+i-1]="*"
for i in range(1,rows+1):
    matrix[rows-i][rows*2-3+i]="*"
for i in range(0,rows):
    matrix[i][(rows*2-2)+rows-1+i]="*"
    
for i in matrix:
    for j in i:
        print(j,end="")
    print()
        
