import random

words = ["FLAVOUR","COLOUR","RAINBOW","COMPUTER","HUMAN","GAME","JUMP","TACKLE","FROZEN"]

def choose(words):
    return random.choice(words)

def jumble(word):
    '''
    w_list = list(word)
    q_list =[]
    
    for i in range(len(w_list)):
        letter = random.choice(w_list)
        q_list.append(letter)
        w_list.remove(letter)
    qn = ''.join(str(x) for x in q_list)
    return qn
    '''
    
    qn = ''.join(random.sample(word,len(word)))       # randomly choosing character from a word --- random.sample(from_which_word,how many times character should be selsected)
    return qn

def check_ans(word):
    ans = input("Guess the word: ")
    
    if ans == word:
        return True 
    else:
        return False
            
def track_point(result,point):
    if result == True:
        point += 1
    return point

def prompt(result,word,player,opp,p_point,o_point):
    if result == True:
        print("\nHey ",player,", you guessed it right. Congratulations. Well played.")
        print("The word is ",word)
    else:
        print("\nSorry ",player,", you couldn't guess it right. Better luck next time.")
        print("The word is ",word)
    print("\nPoints:")
    print(player," : ",p_point)
    print(opp," : ",o_point)

def thank(p1,p2,point_1,point_2):
    print("Thank you, for playing. Have a nice day")
    print("Points:")
    print(p1," : ",point_1)
    print(p2," : ",point_2)
    
def play():
    p1 = input("Player 1, Enter your name: ")
    p2 = input("Player 2, Enter your name: ")
    point_1 = 0
    point_2 = 0
    
    turn = 0
    
    while True:
        # choose a word
        picked_word = choose(words)
        
        # generate a question
        qn = jumble(picked_word)
        print("Jumbled word: ")
        print(qn)
        
        if turn % 2 == 0:
            print("\n",p1," , it is your turn.")
            result = check_ans(picked_word)
            point_1 = track_point(result, point_1)
            prompt(result,picked_word,p1,p2,point_1,point_2)
            
        else:
            print("\n",p2," , it is your turn.")
            result = check_ans(picked_word)
            point_2 = track_point(result, point_2)
            prompt(result,picked_word,p2,p1,point_2,point_1)
        
        choice = input("\nDo you want to continue(y/n): ")
        if choice == "n" or choice == "N":
            thank(p1,p2,point_1,point_2)
            break
        turn += 1
play()