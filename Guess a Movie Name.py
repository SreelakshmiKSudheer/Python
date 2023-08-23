import random
import time
import string

movies = ["avengers","matrix","chichhore","iron man","jungle book","titanic","mission mangal","darkknight","interstellar","interception","the meg","avatar","manichithrathazhu","drishyam"]

secret = random.choice(movies)

life = 10

print("The game is to guess the movie. \nNumber of letters in the movies excluding whitespaces will be given.\nFor every CORRECT guesses the corresponding letter at its position will be shown. |nFor every WRONG guesses ONE LIFE will be DEDUCTED.\nYou are given 10 LIVES at the beginning.\nGame Starts now.")

time.sleep(1)
print("Get Ready..")
time.sleep(1)
print("\nGuess the movie!")
time.sleep(1)




for i in secret:
    if(i == " "):
        print(" ",end = " ")
    else:
        print("_",end = " ")
    
while(life >= 0 ):
    guess = input("\nGuess a letter: ").lower()
    
    for i in secret:
        if(guess == i):
            print(i, end = " ")
        else:
            print("_",end = " ")
    