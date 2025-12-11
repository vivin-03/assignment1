marks = int(input("Enter marks out of 100: "))

if marks >= 95:
    grade = "A+"
elif marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)
