import random
options=['rock','paper','scissor']
user_choise=input("Which one want to choose.'rock','paper',scissor'?: ").lower()
computer_choise=random.choice(options)
print(computer_choise)
if user_choise==computer_choise:
    print("It's draw")
elif user_choise=="rock" and computer_choise=="paper":
    print("Computer own")
elif computer_choise=="rock" and user_choise=="paper":
    print("User own")
elif user_choise=="rock" and computer_choise=="scissor":
    print("User own")
elif computer_choise=="rock" and user_choise=="scissor":
    print("computer own")
elif user_choise=="scissor" and computer_choise=="paper":
    print("User own")
elif computer_choise=="scissor" and user_choise=="paper":
    print("Computer own")
