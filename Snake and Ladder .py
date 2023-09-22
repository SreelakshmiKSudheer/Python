from PIL import Image
import random
end = 100

def show_board():
    img = Image.open('Snake and ladder.png')
    img.show()


def check_ladder(points):
    if points == 8:
        print("Ladder")
        return 26
    elif points == 21:
        print("Ladder")
        return 82
    elif points == 43:
        print("Ladder")
        return 77
    elif points == 50:
        print("Ladder")
        return 91
    elif points == 54:
        print("Ladder")
        return 93
    elif points == 62:
        print("Ladder")
        return 96
    elif points == 66:
        print("Ladder")
        return 87
    elif points == 80:
        print("Ladder")
        return 100
    else:
        return points
    
def check_snake(points):
    if points == 44:
        print("Ladder")
        return 22
    elif points == 46:
        print("Ladder")
        return 5
    elif points == 48:
        print("Ladder")
        return 9
    elif points == 52:
        print("Ladder")
        return 11
    elif points == 55:
        print("Ladder")
        return 7
    elif points == 59:
        print("Ladder")
        return 17
    elif points == 64:
        print("Ladder")
        return 36
    elif points == 69:
        print("Ladder")
        return 33
    elif points == 73:
        print("Ladder")
        return 1
    elif points == 83:
        print("Ladder")
        return 19
    elif points == 92:
        print("Ladder")
        return 51
    elif points == 95:
        print("Ladder")
        return 24
    elif points == 98:
        print("Ladder")
        return 28
    else:
        return points


def reached_end(points):
    if points == end:
        return True
    else:
        return False


def play():
    p1_name = input('Player 1, Please enter your name: ')

    p2_name = input('Player 2, Please enter your name: ')
    
    pp1 = 0
    pp2 = 0
    
    turn = 0
    
    while True:
        
        if turn % 2 == 0:
            print(p1_name,", its your turn: ")
            # ask player's choice to continue
            c = input("\nPress 1 to continue and 0 to quit: ")
            
            if c == 0:
                print("\nScore:")
                print("\t",p1_name," : ",pp1)
                print("\t",p1_name," : ",pp2)
                print("Quitting the game, Thanks for playing")
                break
            # generate a random number
            dice = random.randint(1,6)
            print("\nDice showed: ",dice)
            
            pp1 = pp1 + dice
            
            pp1 = check_ladder(pp1)
            pp1 = check_snake(pp1)
            
            if pp1 > end:
                pp1 = end
            print(p1_name,", Your score: ",pp1)
            if reached_end(pp1):
                print(p1_name," won")
                break
        else:
            print(p2_name,", its your turn: ")
            # ask player's choice to continue
            c = input("\nPress 1 to continue and 0 to quit: ")
            
            if c == 0:
                print("\nScore:")
                print("\t",p2_name," : ",pp2)
                print("\t",p2_name," : ",pp2)
                print("Quitting the game, Thanks for playing")
                break
            # generate a random number
            dice = random.randint(1,6)
            print("Dice showed: ",dice)
            
            pp2 = pp2 + dice
            
            pp2 = check_ladder(pp1)
            pp2 = check_snake(pp1)
            
            if pp2 > end:
                pp2 = end
            print(p2_name,", Your score: ",pp2)
            if reached_end(pp2):
                print(p2_name," won")
                break
        turn += 1
show_board()
play()