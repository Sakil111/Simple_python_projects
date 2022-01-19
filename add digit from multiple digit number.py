# calculate total of mulitple digit number
multiple_digit_number=input("Enter multiple digit number: ")
number=list(multiple_digit_number)
total=0
for i in number:
    sum=int(i)
    total+=sum
print(total)

# calculate total of two digit number
two_digit_number=input("enter two digit number: ")
first_number=int(two_digit_number[0])
second_number=int(two_digit_number[1])
total=first_number+second_number
print(total)
