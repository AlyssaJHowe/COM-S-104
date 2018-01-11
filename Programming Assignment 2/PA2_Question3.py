#Interactive script that allows a user to actually partake in the "penny game"

from games import *
display_menu()
user_choice = raw_input("Enter your choice: ")

#While loop allows user to continue playing until they press "q".
while user_choice == "p":
    pn1 = place_penny()
    pn2 = place_penny()
    print "Player1:", pn1
    print "Player2:", pn2

    while pn1 != pn2:
        print "Game Continue..."
        pn1 = place_penny()
        pn2 = place_penny()
        print "Player1:", pn1
        print "Player2:", pn2
        
    if pn1 and pn2 == "Head":
        print "Player 1 wins the game."
    if pn1 and pn2 == "Tail":
        print "Player 2 wins the game."
    display_menu()
    user_choice = raw_input("Enter your choice: ")
        
else:
    print "Bye!!!"
    
