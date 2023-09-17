nums = []

n = int(input("How may numbers? "))

def read():
    print("Enter the numbers:")
    for i in range(n):
        num = int(input())
        nums.append(num)
        
def linear_search():
    key = int(input("Enter the number to be searched: "))
    
    present = 0
    
    for i in range(n):
        if(nums[i] == key):
            print(key, " is present at the position ",i+1)
            present = 1
            break
    if(not present):
        print(key, " is not present")
        
read()
linear_search()