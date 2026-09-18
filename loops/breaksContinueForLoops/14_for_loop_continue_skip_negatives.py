import random
"""
Task: Skip Negatives
Concepts: for loop, continue

Loop through a list of numbers (mix of positive and negative).
Use `continue` to skip negative numbers, and print only the positive ones.
"""

# Create a list of numbers (mix of positive and negative).
# Loop through them and print only the positive ones
# but do it using continue to skip negative numbers, instead of an if that only prints when positive.

list_numbers = random.sample(range(-100, 100), 21)

for index in list_numbers:
    if index < 0:
        continue
    print(index)
