import random

doors = [0] * 3
goatdoor = [0] * 2

swap = 0                # no. of swap wins
dont_swap = 0           # no. of don't swap wins

count = 0
while count < 10:
    x = random.randint(0, 2)
    doors[x] = "BMW"

    for i in range(3):
        if(i == x):                 # doors[x] = "BMW" therefore we don't consider it in this loop 
            continue
        else:
            doors[i] = "Goat"       # doors[i] = "Goat" where i not equal to x
            goatdoor.append(i)      # tracking the index of the door where goat is present

    choice = int(input("Enter your choice: "))
    door_open = random.choice(goatdoor)         # open a door that comprises of goat

    while(door_open == choice):                 # door_open should not be equal to choice
        door_open = random.choice(goatdoor)
        
    ch = input("Do you want to swap(y/n): ")
    if(ch == "y"):
        if(doors[choice] == "Goat"):
            print("Player wins")
            swap += 1
        else:
            print("Player lost")
    else:
        if(doors[choice] == "Goat"):
            print("Player lost")
        else:
            print("Player wins")
            dont_swap += 1
            
    print("Swap wins : ",swap)
    print("DOn't Swap wins : ",dont_swap)
    
    count += 1