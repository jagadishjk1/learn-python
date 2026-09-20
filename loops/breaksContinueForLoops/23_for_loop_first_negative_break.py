"""
Task: First Negative Number
Concepts: for loop, break, if-else, flag variable

Loop through a list of numbers and find the FIRST negative number
in the list. Once found, print it and break immediately. If there
are no negative numbers at all, print a message saying so.
"""
import random
list_numbers = random.sample(range(-30,30), 40)

for number in list_numbers:
    if number < 0:
        print(f"first negitive number in the list is: {number}")
        break
else:
    print("No negative numbers found.")
