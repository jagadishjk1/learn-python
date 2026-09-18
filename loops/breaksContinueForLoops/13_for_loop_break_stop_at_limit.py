import random
"""
Task: Stop at a Limit
Concepts: for loop, break

Loop through a list of numbers, print each one, and stop completely
using break as soon as a number greater than 50 is encountered.
"""
# Create a list of numbers. 
# Loop through them and print each one, but stop completely (using break) as soon as you hit a number greater than 50.

list_numbers = random.sample(range(-40, 66), 50)
break_number = 50

#checking the random list 
print(list_numbers)

#loops starts here
for n in list_numbers:
    if n > 50:
        print(f'value {n} is greater than 50')
        break
    print(n)
