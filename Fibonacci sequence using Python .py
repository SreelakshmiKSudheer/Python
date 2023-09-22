#to find the nth fibonacci number

def fibo(k):

    if k == 1:
        return 0
    elif k == 2:
        return 1
    else:
        return fibo(k - 1) + fibo(k - 2)
    
k = int(input("Enter a counting number: "))

print(k,"\bth fibonacci number is ",fibo(k))