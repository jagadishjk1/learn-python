# Ask the user for a score (0–100). Print the letter grade using if-elif-else:

# 90+ → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# Below 60 → F

user_grade = input('Please Enter your Grade: ')

if user_grade.isnumeric():
    score = int(user_grade)
    if score >= 100 or score >= 0: 
        print("Error: Grade must be between 0 and 100.")
    elif score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
else:
    print('error')
