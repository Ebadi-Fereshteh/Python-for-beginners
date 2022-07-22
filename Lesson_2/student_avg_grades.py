print("Enter the number of students:")
count = int(input())
grades = []
for i in range (count):
    print("grade ",i+1,":")
    grade = float(input())
    grades.append(grade)
s = sum(grades)
print("avg: ",(s/count))
print("min: ",min(grades))
print("max: ",max(grades))
