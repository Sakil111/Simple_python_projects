print("Welcome to the treasure island game")
path=input("which way do you want to go? 'left' or 'right': ").lower()
if path=="left":
    way=input("No boat now, do you and to 'wait' or 'swim': ").lower()
    if way=="wait":
        door=input("which door you want to enter: 'blue','red','yellow': ").lower()
        if door=="yellow":
            print("You win the game")
        else:
            print("You lose the game")

    else:
        print("Game is over")

else:
    print("Game is over")