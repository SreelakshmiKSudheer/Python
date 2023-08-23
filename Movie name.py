import random
import time
import string

movies = ["avengers","matrix","chichhore","iron man","jungle book","titanic","mission mangal","darkknight","interstellar","interception","the meg","avatar","manichithrathazhu","drishyam"]


def play():
    p1 = input("Player 1 : Enter your name: ")
    p2 = input("Player 2 : Enter your name: ")
    
    pp1 = 0
    pp2 = 0
    
    turn = 0
    
    willing = 1
    while willing:
        
        secret = random.choice(movies)
        
        
        
        if(turn % 2 == 0):
           #player 1
           print(p1,", its your turn")
           qn = create_question(picked)
           print(qn)
           
           not_said = 1 
           while not_said:
               letter = input("Your letter: ")
               if(is_present(letter,picked_movie)):
                   #unlock
            else:
                print(letter," not found")
        else:
            #player 2
            print(p2,", its your turn")