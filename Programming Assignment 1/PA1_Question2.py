#This script is meant to emulate a 2-player game of rock, paper, scissors.
from random import choice
while True:
    raw_input("Player 1: Press ENTER to display a hand.")
    player1 = choice(["Scissors","Paper","Rock"])
    print "Player 1, you played " + player1 + "!"
    raw_input("Player 2, your turn: Press ENTER to display a hand.")
    player2 = choice(["Scissors","Paper","Rock"])
    print "Player 2, you played " + player2 + "!"
    if player1 == "Scissors" and player2 == "Scissors":
        print "It's a draw!"
    elif player1 == "Scissors" and player2 == "Paper":
        print "Player 1 wins!"
    elif player1 == "Scissors" and player2 == "Rock":
        print "Player 2 wins!"
    if player1 == "Rock" and player2 == "Rock":
        print "It's a draw!"
    elif player1 == "Rock" and player2 == "Scissors":
        print "Player 1 wins!"
    elif player1 == "Rock" and player2 == "Paper":
        print "Player 2 wins!"
    if player1 == "Paper" and player2 == "Paper":
        print "It's a draw!"
    elif player1 == "Paper" and player2 == "Rock":
        print "Player 1 wins!"
    elif player1 == "Paper" and player2 == "Scissors":
        print "Player 2 wins!"
    again = raw_input("Do you want to play again (y/n)? ")
    if again == "n":
        break
    
