"""
Task: Menu System
Concepts: while True, break, continue, if-elif-else

Show a menu with options. Keep showing it until the user chooses
to exit. Handle invalid choices gracefully using continue.
"""
from datetime import date
today = date.today()

while True:
    print("=" * 10 , "#" * 5, "=" * 10)
    user_input = input("Please select the option from below menu:\n" "Press 1 : Say Hello\n""Press 2: Show today's date\n" "Press 3 : Exit\n" "Waiting for your input: ")
    print("\n")
    if user_input == "1":
        print("Hello my friend!")
    elif user_input == "2":
        print(f"Todays date: {today}")
    elif user_input == "3":
        print("Exiting the system.")
        break
    else:
        print("Invaild input, Please try again!")
        continue