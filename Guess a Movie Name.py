import random
import time
import string

# movie list
movies = []
english = ["darkknight","interstellar","interception","the meg","avatar","matrix","avengers","avengers : endgame","jurassic park","jurassic world","iron man","jungle book","titanic"]
malayalam = ["manichithrathazhu","drishyam","sandesham","kireedam","vanaprastham","christian brothers","bhaskar the rascal"]
tamil = ["bigil","anjaan","kaththi","mersal","maari"]
telegu = ["bahubali: the beginning","bahubali: the conclusion"]
hindi = ["mission mangal","chichhore","chennai express"]

movies.extend(english)
movies.extend(malayalam)
movies.extend(tamil)
movies.extend(telegu)
movies.extend(hindi)

# terminating condition ( to keep track whether the user guessed the movie correctly)
matching = False

# to limit the number of tries
life = 10

count = 0

# instruction to the user
print("The game is to guess the movie. \nNumber of letters in the movies excluding whitespaces will be given.\nFor every CORRECT guesses the corresponding letter at its position will be shown. |nFor every WRONG guesses ONE LIFE will be DEDUCTED.\nYou are given 10 LIVES at the beginning.\nGame Starts now.")

# player name
pname = input("\nEnter your name: ")

# language choice
lang_choice = input("Do you have any language preferences(y/n): ").lower()



# secret movie chosen randomly
if(lang_choice == "y"):
    # select language
    lang = input("Enter preferred language(English/Malayalam/Hindi/Tamil/Telugu): ").lower()

    if(lang == "english"):
        secret = random.choice(english)
    elif(lang == "malayalam"):
        secret = random.choice(malayalam)
    elif(lang == "tamil"):
        secret = random.choice(tamil)
    elif(lang == "talugu"):
        secret = random.choice(telegu)
    elif(lang == "hindi"):
        secret = random.choice(hindi)
else:
    secret = random.choice(movies)

# for tracking purpose 
intermediate = []
for i in secret:
    if(i == " "):
        intermediate.append(" ")
    elif(i == ":"):
        intermediate.append(":")
    elif(i == ","):
        intermediate.append(",")
    else:
        intermediate.append("_")
    

time.sleep(1)
print("\nGet Ready..")
time.sleep(1)
print("\nGuess the movie!")
time.sleep(1)

j = 0
for i in secret:
    print(intermediate[j],end = " ") 
    j += 1 
print("\n")
# game starts from here    
while(life > 0 and matching == False):

    matching = True

    guess = input("\nGuess a letter: ").lower()
    
    # letter guess correctness
    letter_matching = False

    j = 0
    for i in secret:
        if(guess == i):
            intermediate[j] = guess
            letter_matching = True
        j += 1

    if(letter_matching == False):
        life -= 1
    # guess the entire movie if the player wants
    count += 1

    j = 0
    for i in secret:
        print(intermediate[j],end = " ") 
        j += 1 
    
    
    if(count % 2 == 0):
        guess_movie_choice = input("\nGot the movie(y/n)? ").lower()
        if(guess_movie_choice == "y"):
            guess_movie = input("Enter the movie: ")
            if(guess_movie == secret):
                matching = True
                break

    # checking whether the user guessed the entire movie
    j = 0
    for i in secret:
        if(intermediate[j] != i):
            matching = False
            break
        j += 1
    
    print("\nLife = ",life," \n")

if(matching == True):
    print("\nHey ",pname,", You guessed it right. Congratulations ...")
    print("The movie is ",secret)
else:
    print("\nSorry ",pname,", You couldn't figure it out. Better luck next time...")
    print("The movie is ",secret)
