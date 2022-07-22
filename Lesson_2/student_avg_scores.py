print("Enter the number of students:")
count = int(input())
scores = []
for i in range (count):
    print("score ",i+1,":")
    score = float(input())
    scores.append(score)
s = sum(scores)
print("avg: ",(s/count))
print("min: ",min(scores))
print("max: ",max(scores))
