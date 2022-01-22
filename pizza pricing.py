size=input("What size of pizza do you want? s,m,l: ")
add_preparoni=input("Do you want to add preparoni? y,n: ")
extra_cheese=input("Do you want extra cheese? y,n: ")
bill=0
if size=="s":
    bill+=15
elif size=="m":
    bill+=20
elif size=="l":
    bill+=25
if add_preparoni=="y":
    if size=="s":
        bill+=2
    else:
        bill+=3

if extra_cheese=="y":
    bill+=1

print(f"your final bill is {bill}")