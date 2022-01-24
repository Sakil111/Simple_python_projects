print("Welcome to Hangman")
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
word_list=["popular","baboon","camel"]
chosen_word=random.choice(word_list)
word_lsit=["popular","baboon","camel"]
chosen_word=random.choice(word_lsit)
print(chosen_word)
lives=6
display=[]
for letter in range(len(chosen_word)):
    display+="_"
print(display)

end_of_game=False
while not end_of_game:

    guess=input("choose a letter: ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    print(display)
    if "_" not in display:
        end_of_game=True
        print("You win the game")

    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose the game")

    print(stages[lives])

