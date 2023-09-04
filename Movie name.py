import random
import string

movies = ["avengers","matrix","chichhore","iron man","jungle book","titanic","mission mangal","darkknight","interstellar","interception","the meg","avatar","manichithrathazhu","drishyam"]

def create_question(movie):
	n = len(movie)
	letters = list(movie)
	temp = []
	for i in range(n):
		if letters[i] == ' ':
			temp.append(' ')
		else:
			temp.append('*')
	qn = ''.join(str(x) for x in temp)
	return qn

def is_present(letter,movie):
	c = movie.count(letter)
	if c == 0:
		return False
	else:
		return True
	

def unlock(qn,movie,letter):
	ref = list(movie)
	qn_list = list(qn)
	temp = []
	n = len(movie)
	for i in range(n):
		if ref[i] == ' ' or ref[i] == letter:
			temp.append(ref[i])
		else:
			if qn_list[i] == '*':
				temp.append('*')
			else:
				temp.append(ref[i])
	qn_new = ''.join(str(x) for x in temp)
	return qn_new


def play():
    p1 = input("Player 1 : Enter your name: ")
    p2 = input("Player 2 : Enter your name: ")
    
    pp1 = 0
    pp2 = 0
    
    turn = 0
    
    willing = 1
    while willing:

        if(turn % 2 == 0):
            #player 1
            print(p1,", its your turn")
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
           
            not_said = True 
	    
            while not_said:
                letter = input("Your letter: ")
                if(is_present(letter,picked_movie)):
                    #unlock
                    modified_qn = unlock(modified_qn,picked_movie,ch)
                    print(modified_qn)
           		
                    decision = input("Press 1 to guess the movie or 2 to unlock the next character")
           		
                    if decision  == 1:
           		        ans = input("Enter the movie")
                        if(ans == picked_movie):
                            pp1 += 1
                            print("Correct")
                            not_said = False
                            print(p1, " your score = ",pp1)
                        else: 
           		            print("Wrong answer. Try again")
           		else:
                    print(letter," not found")
		
            c = input("Press 1 to continue or 2 to quit")
			
            if c == 0:
                willing = False
                print(p1," your score : ",pp1)
                print(p2, " your score = ",pp2)
                print("Thanks for playing.\n Have a nice day")		
        else:
            			#player 2
            print(p2,", its your turn")
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
           
            not_said = True 
	    
            while not_said:
                letter = input("Your letter: ")
                if(is_present(letter,picked_movie)):
                    #unlock
                    modified_qn = unlock(modified_qn,picked_movie,ch)
                    print(modified_qn)
           		
                    decision = input("Press 1 to guess the movie or 2 to unlock the next character")
           		
                    if decision  == 1:
               		    ans = input("Enter the movie")
                        if(ans == picked_movie):
                            pp2 += 1
                            print("Correct")
                            not_said = False
                            print(p2, " your score = ",pp2)
                        else: 
               		        print("Wrong answer. Try again")
           	    else:
                    print(letter," not found")
		
            c = input("Press 1 to continue or 2 to quit")
			
            if c == 0:
                willing = False
                print(p1," your score : ",pp1)
                print(p2, " your score = ",pp2)
                print("Thanks for playing.\n Have a nice day")
        turn += 1            

play()
