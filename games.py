#This script contains the function for the "penny game".
#It chooses a random number and based on whether the number is even or odd, Python returns head or tails.
from random import randint

def place_penny():
    r = randint(1,10)
    if r % 2 == 0:
        return "Head"
    else:
        return "Tail"

#Simple function that when called, displays a menu to the user.
def display_menu():
    print "###MENU### \n p) Play the matching penny game \n q) Quit"
    
