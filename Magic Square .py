
def magic_square(n):
    
    MSquare = []
    for i in range(n):
        l = []
        for j in  range(n):
            l.append(0)
        MSquare.append(l)
    
    m = n*(n**2 + 1)//2
        
    i = n//2
    j = n-1
    count = 1
    num = n*n
    
    while(count <= num):
        if(i == -1 and j == n): # Condition 4
            j = n-2
            i = 0
        else:
            if(j == n):         # column value exceeding case
                j = 0
            if(i < 0):          # when row < 0
                i = n - 1
        
        if(MSquare[i][j] != 0): 
                j = j - 2
                i = i + 1
                continue
        else:
            MSquare[i][j] = count
            count += 1
        
        i = i - 1
        j = j + 1       #Condition 1
    
        
    for i in range(n):
        for j in  range(n):
            print(MSquare[i][j],end = "\t")      # print in one line items seperated by whitespace
        print()
        
    print("The sum of each row/column/diagonal = ",m)
        
N = int(input("Enter the dimension: "))

if(N % 2 == 0):
    print("Magic Square formation not possible")
else:
    magic_square(N)


'''
N = int(input("Enter the dimension: "))
magic = [[0 for i in range(N)]for j in range(N)] 
print(magic)
'''