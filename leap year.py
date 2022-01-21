# here we are checking a year is it leap year or not.
year=int(input("Enter a year: "))

if year%4==0:
    if year % 100 == 0:
        if year%400==0:
            print("Leap year")
        else:
            print("Not Leap year")
    else:
        print("leap year")

else:
    print("Not leap year")
