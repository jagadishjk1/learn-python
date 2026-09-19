"""
Task: Combine Break and Continue
Concepts: for loop, break, continue

Loop through a list of numbers:
- Skip (continue) any negative numbers
- Stop (break) completely once a number greater than 100 is encountered
- Print every number that isn't skipped or doesn't trigger the stop
"""

# Create a list of numbers. Loop through them:

# Skip (using continue) any negative numbers
# Stop (using break) completely once you encounter a number greater than 100
# Print every number that doesn't get skipped or trigger the stop
import random

number_list = random.sample(range(-20, 104), 49)

#print number list to validate the loop
print(number_list)

for number in number_list:
    if number > 100:
        break
    if number < 0:
        continue
    print(number)

