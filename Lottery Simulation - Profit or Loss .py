import random
import matplotlib.pyplot as plt

account = 0
x = []
y = []

for i in range(365):
    x.append(i+1)
    bet = random.randint(1,10)
    lucky_draw = random.randint(1,10)
    if bet == lucky_draw:
        account += 900-100
    else:
        account -= 100
    
    y.append(account)
    
    #print("Bet : ",bet)
    #print("Lucky draw : ",lucky_draw)    
print("Your account : ",account)
plt.plot(x,y)
    
