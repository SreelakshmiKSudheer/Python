def binary_search(a,key):
    
    l = 0
    r = len(a) - 1
    present = 0
    
    while(l < r and present == 0):
        
        mid = (l + r) // 2
        
        if(a[mid] == key):
            present = 1
            return mid
        elif(key < a[mid]):
            r = mid - 1
        else:
            l = mid + 1
    return -1

def play():
    
    a = []
    
    for i in range(1,100000):
        a.append(i)
        
    key = int(input("Enter the number to be searched: "))
    
    result = binary_search(a, key)
    
    if(result >= 0):
        print("")