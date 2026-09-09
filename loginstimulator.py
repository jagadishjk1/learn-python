# Simple Login Simulator
# Store a correct username and password as variables. Ask the user to input both. Check:

# Both correct → "Login successful"
# Username correct but password wrong → "Wrong password"
# Username wrong → "User not found"
correct_username = "rossi"
correct_password = "12345"

username = str(input('Please enter your username: '))
user_password = input('Please enter your password: ')

if username == correct_username and user_password == correct_password:
    print(f"user: {username} is successfully logged in. Enjoy browsing!")
elif username == correct_username and user_password != correct_password:
    print(f"Wrong password, Please try again.")
else:
    print(f"User not found, Please try again.")