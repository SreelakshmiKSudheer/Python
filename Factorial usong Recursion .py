def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f *= i
        
    return f
        
n = int(input("Enter a counting number: "))
if n < 0:
    print("Factorial not defined")
else:
    print(n,"\b! = ",fact(n))