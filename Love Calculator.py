name1=input("What is your name?: ").lower()
name2=input("What is their name? : ").lower()
t=name1.count("t")
r=name1.count("r")
u=name1.count("u")
e=name1.count("e")
l=name2.count("l")
o=name2.count("o")
v=name2.count("v")
e=name2.count("e")
true=t+r+u+e
love=l+o+v+e
love_score=int(str(true)+str(love))
if love_score>90 or love_score<10:
    print(f"Your score is {love_score}%, you got together coke and mentors")
elif love_score<40 and love_score>60:
    print(f"Your score is {love_score}%, you are alright together")
else:
    print(f"Your score is {love_score}%")
