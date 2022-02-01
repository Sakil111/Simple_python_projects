# Choosing a random number from 1 to 100
import random
print("Number is between 1 to 100")


def check_answer(guess, answer,turns):
    if guess > answer:
        print("It's too high")
        return turns -1
    elif guess < answer:
        print("It's to low")
        return turns -1
    else:
        print(f"You got it, The answer is {answer}")

answer=random.randint(1,100)
EASY_LEVEL=10
HARD_LEVEL=5
# Make function to set difficulty
def set_difficulty():
    level=input("Choose difficulty type 'easy' or 'hard': ")
    if level=="easy":
        return EASY_LEVEL
    elif level=="hard":
        return HARD_LEVEL

def game():
    # Function to check user's guess number with actual number

    turns=set_difficulty()


    # Track the number and reduce the number if it guess is wrong
    # repeat the process if it guess wrong or if we get the right the game then end the game
    guess=0
    while guess !=answer:
        print(f"You have got {turns} attempts")
        # Let's user guess a number
        guess = int(input("Make a guess: "))
        turns=check_answer(guess, answer,turns)
        if turns ==0:
            print("You have run out of the guess, you lost")
            return
game()