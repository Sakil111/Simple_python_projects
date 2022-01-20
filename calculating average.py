students_height=input("Enter list of students heights: ").split()

for i in range(0,len(students_height)):
    students_height[i]=int(students_height[i])

print(students_height)
# calculating total height
total=0
for height in students_height:
    total+=height
print(total)

# calculating number of students
number_of_students=0
for student in students_height:
    number_of_students+=1
print(number_of_students)

# calculating average
average=total/number_of_students
print(average)
