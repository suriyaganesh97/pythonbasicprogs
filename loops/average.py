student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
sumOfHeight = 0
count = 0
for height in student_heights:
    sumOfHeight += height
    count += 1
print(round(sumOfHeight/count))
