# Task 3 — Username Validator
# Ask the user to input a username. Check and print whether:

# It's at least 5 characters long
# It contains no spaces
# It starts with a letter (not a number)

username = str(input('Please Enter your Username: '))

if (len(username) >= 5 and username[0].isalpha()) and " " not in username:
    print(f'{username} is valid username')
else:
    print("please provide valid username, Try again!")