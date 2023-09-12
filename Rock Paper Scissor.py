def rock_paper_scissor(num1,num2,bit1,bit2):
    p1 = int(num1[bit1]) % 3
    p2 = int(num2[bit2]) % 3
    
    if(player_1[p1] == player_2[p2]):
        print("Draw\n")
    elif(player_1[p1] ==  "Rock" and player_2[p2] == "Paper"):
        print("Player 2 wins\n")
    elif(player_1[p1] ==  "Rock" and player_2[p2] == "Scissor"):
        print("Player 1 wins\n")
    elif(player_1[p1] ==  "Paper" and player_2[p2] == "Rock"):
        print("Player 1 wins\n")
    elif(player_1[p1] ==  "Paper" and player_2[p2] == "Scissor"):
        print("Player 2 wins\n")
    elif(player_1[p1] ==  "Scissor" and player_2[p2] == "Rock"):
        print("Player 2 wins\n")
    elif(player_1[p1] ==  "Scissor" and player_2[p2] == "Paper"):
        print("Player 1 wins\n")
        
        
player_1 = {0:"Rock", 1 : "Paper", 2 : "Scissor"}       # defines the secret code
player_2 = {0:"Rock", 1 : "Paper", 2 : "Scissor"}

while True:
    num1 = input("Player 1, Enter your choice: ")       # for 10 digit number -- inputs as a string
    num2 = input("Player 2, Enter your choice: ")
    
    bit1 = int(input("Player 1, Enter the secret bit position: "))      # position of the digit chosen in the 10 digit number
    bit2 = int(input("Player 2, Enter the secret bit position: "))
    
    rock_paper_scissor(num1,num2,bit1,bit2)
    
    ch = input("DO you want to continue(y/n) : ")
    if(ch == "n"):
        break
    