scores=input("Enter list of students score: ").split()
for i in range(0,len(scores)):
    scores[i]=int(scores[i])
print(scores)

height_score=0
for score in scores:
    if height_score<score:
        height_score=score
print(height_score)