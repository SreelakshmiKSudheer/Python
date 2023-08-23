import string
import random

N = int(input("Enter the number of elements in a list: "))

symbols = []
symbols = list(string.ascii_letters)
list_1 = [0] * N
list_2 = [0] * N


#pos1 and pos2 are same symbol positions in the list 1 and 2
pos1 = random.randint(0,N - 1)      # 0 <= rand <= n-1
pos2 = random.randint(0,N - 1)



samesymbol = random.choice(symbols)
symbols.remove(samesymbol)


if (pos1 == pos2):
    list_1[pos1] = samesymbol
    list_2[pos1] = samesymbol
else:
    list_1[pos1] = samesymbol
    list_2[pos2] = samesymbol
    list_1[pos2] = random.choice(symbols)
    symbols.remove(list_1[pos2])
    list_2[pos1] = random.choice(symbols)
    symbols.remove(list_2[pos1])
    
    
i = 0
while(i < N):
    if(i != pos1 and i != pos2):
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)
        
        list_1[i] = alphabet1
        list_2[i] = alphabet2
        
    i += 1
    
print(list_1)
print(list_2)

choice = input("Enter the similiar symbol: ")
if(choice == samesymbol):
    print("Hurray! Its correct. Well done")
else:
    print("Sorry! That's wrong. Better next time")
