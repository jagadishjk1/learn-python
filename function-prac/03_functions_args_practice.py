"""
Task: *args Practice
Concepts: functions, *args, return

Write a function that accepts any number of numbers (using *args)
and returns their total sum. Test it by calling it with 2 numbers,
then 5 numbers, then 0 numbers.
"""

def sum_numbers(*args):
    sum_of_numbers =sum(args)
    return sum_of_numbers

total_sum_of_numbers = sum_numbers(23,45,44,67)
print(total_sum_of_numbers)
