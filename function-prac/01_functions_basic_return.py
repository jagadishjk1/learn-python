# 01_functions_basic_return.py

"""
Task: Basic Function with Return
Concepts: functions, parameters, return

Write a function that takes two numbers as parameters and returns
their sum (not print it — return it). Call the function with a few
different number pairs and print the results.
"""

def number_pair(a, b):
    x = a + b
    return x

a_value = int(input("Please enter first value: "))
b_value = int(input("Please enter second value: "))
x_value = number_pair(a_value, b_value)

print(x_value)