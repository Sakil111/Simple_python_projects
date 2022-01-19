hegiht=int(input("Enter your height in cm: "))
price=0
if hegiht>120:
    age = int(input("Enter your age: "))
    if age <12:
        price=5
    elif age<18:
        price=7
    else:
        price=12
    want_photo=input("type 'y' for photo,type 'n' if not: " )
    if want_photo=="y":
        price+=3
else:
    print("Are not eligible for ride")

print(f"your total price is {price}")
