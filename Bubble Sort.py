numbers = []
n = int(input("How many numbers: "))

def read():
    
    print("Enter numbers:")
    for i in range(n):
        num = int(input())
        numbers.append(num)
    
def bubble_sort():
    for i in range(n):
        for j in range(n-i-1):
            if(numbers[j] > numbers[j+1]):
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
read()
bubble_sort()         
print(numbers)