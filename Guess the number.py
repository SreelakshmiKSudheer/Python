import random

print("The game is to guess the number. The number is between 1 to 100000")
print("You have 20 attempts to guess it correct")
print("You can enter numbers, computer will tell whether it is equal to, greater than or less than the secret number")
print("Get Ready")

count = 0
correct = False

secret = random.randint(1, 100000)
numbers = []
for i in range(1,100001):
    numbers.append(i)

while(count < 20 and correct == False):
    guess = int(input("Guess :"))
    
    if(guess == secret):
        print("Hey you guessed it right")
    elif(secret < guess):
        print("< ",guess)
    else:
        print("> ",guess)

    