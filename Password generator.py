#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("welcome to the password generator")
number_of_letters=int(input("Enter how many number would you like in your password:\n "))
number_of_numbers=int(input("Enter how many letters would you like in your password:\n "))
number_of_symbols=int(input("Enter how many symbols would you like in your password:\n "))

password_list=[]
for letter in range(0,number_of_letters):
    password_list+=random.choice(letters)
for number in range(0,number_of_numbers):
    password_list+=random.choice(numbers)
for symbol in range(0,number_of_symbols):
    password_list+=random.choice(symbols)

random.shuffle(password_list)

password=""
for char in password_list:
    password+=char
print(f"Your password is:  {password}")
