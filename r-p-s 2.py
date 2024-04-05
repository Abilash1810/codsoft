import random
print("vaid moves")
print("1.rock")
print("2.paper")
print("3.scissors")
def lets_play():
    player1_move=str(input("choose any one move :",))
    if player1_move in ["rock" ,"paper", "scissors"]:
        print("choice of player1 is:",player1_move)
    else:
        print("choose a valid move")
    onlineplayer= random.choice(["rock","paper","scissors"])
    print("choice of online player is:",onlineplayer)
    player1_score=0
    onlineplayer_score=0
    if player1_move==onlineplayer:
        print("It's a tie")
    elif (player1_move=="rock" and onlineplayer=="scissors") or (player1_move=="scissors" and onlineplayer=="paper") or (player1_move=="paper" and onlineplayer=="rock"):
        print( "Player1 wins")
        player1_score+=1
    else:
        print("online player wins")
        onlineplayer_score+=1
    print("player1 score is :",player1_score)
    print("online player score is :",onlineplayer_score)
    if (player1_score>onlineplayer_score):
        print("player1 wins the game")
    elif (player1_score==onlineplayer_score):
        print("it's a tie")
    else:
        print("online player wins the game")
lets_play()
print("if you want to play again type yes")
player_choice=str(input("Tell us your decision :",))
if player_choice=="yes":
          lets_play()
else:
    print("Have a Great Day")
                  

    
    
