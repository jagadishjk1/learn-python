"""
Task: Password Strength Checker
Concepts: for loop, break, if-elif-else, string methods (isalpha, isnumeric)

Ask the user for a password. Loop through each character and check
if it contains at least one digit and at least one special character.
As soon as both conditions are satisfied, stop checking early using break.
Print whether the password is "Strong" or "Weak" based on the result.
"""
user_password = input('Please Enter your new password: ')

password_digit = 0
password_charac = 0


for password in user_password:
    if not password.isalnum():
        password_charac += 1
    if password.isnumeric():
        password_digit += 1
    if password_digit >= 1 and password_charac >= 1:
        break

# print(password_digit)
# print(password_charac)
if password_digit >= 1 and password_charac >= 1:
    print("This password is strong. continue..")
else:
    print("This password is weak. Please try again.")