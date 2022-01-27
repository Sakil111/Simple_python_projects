import random
names=input("Give everybody's name: ").split(" ")
index=random.randint(0,len(names)-1)
person=names[index]
print(f"{person} you are going to pay")