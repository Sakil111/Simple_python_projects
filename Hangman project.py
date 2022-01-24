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
# Generate a random word
word_list=["apple","help","introduce"]
chosen_word=random.choice(word_list)
word_len=len(chosen_word)
live=6
# Generating blank in the list
end_of_game=False
display=[]
for i in range(word_len):
    display+="_"
print(display)
print(chosen_word)

# Guessing letter and selecting the letter until correct word is available.
while not end_of_game:
    guess_letter=input("Guess a letter: ").lower()
    for position in range(word_len):
        letter=chosen_word[position]
        if letter==guess_letter:
            display[position]=letter

    print(display)
    if "_" not in display:
        end_of_game=True
        print("You won the game")
    if guess_letter not in chosen_word:
        live-=1
        print("You lose a live")
        if live ==0:
            end_of_game=True
            print("End of the game,You lose the game")
    print(stages[live])



