from datetime import date

NAME = input("Enter you name: ")
AGE = int(input("Enter your age: "))
CURRENT_YEAR = date.today().year
# print(CURRENT_YEAR)
CAL_BORN_YEAR = int(CURRENT_YEAR - AGE)
print(f"Hi {NAME}, you are {AGE} years old and were likely born around {CAL_BORN_YEAR}.")