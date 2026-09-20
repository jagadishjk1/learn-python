"""
Task: Skip and Stop Together
Concepts: for loop, break, continue, if-elif-else

Loop through a list of numbers. Skip (continue) any number that is
a multiple of 5. Stop (break) completely once you've printed 5
numbers total (not counting the skipped ones). Print each number
that isn't skipped.
"""
import random
list_of_numbers = random.sample(range(10, 101), 49)
print(list_of_numbers)
number_seq = 0

for number in list_of_numbers:
    if number % 5 == 0:
        continue
    elif number_seq == 5:
        break
    else:
        print(number)
        number_seq += 1