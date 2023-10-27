'''
# sorting a list a function

#x = [1,2,4,3]                      #int list
#x = ['a','e','j','x']              #char ist
x = {'q': 1, 'w':2, 'e':4, 't': 0}  # based on the key values
print(sorted(x))                    # sorted list
print(sorted(x, reverse = True))    #reverses the sorted list or sorted list in the ascending order

L = ["cccc","bb","a","ddd"]
print(sorted(L,key = len))          # sorts in the ascending order of length
'''

str1 = input("Enter string 1: ")
str2 = input("Enter string 1: ")

if(sorted(str1) == sorted(str2)):
    print("Anagrams")
else:
    print("NOt anagrams")