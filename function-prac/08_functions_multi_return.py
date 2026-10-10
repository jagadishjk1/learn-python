"""
Task: Multi-Value Return
Concepts: functions, return multiple values, loops (manual comparison)

Write a single function that takes a list of numbers and returns
the minimum, maximum, and average — all three, in one return statement.
"""
import random
#Function
def analyze_number(numbers):
    min_val=list_number[0]
    max_val=list_number[0]
    count=0
    total_sum = 0

    for num in numbers:
        if num < min_val:
            min_val = num
        
        if num > max_val:
            max_val = num

        total_sum += num
        count += 1
    average_val = total_sum / count
    return min_val, max_val, average_val 




list_number = random.sample(range(10, 50), 20)
print(list_number) 
min_value, max_value, average_value = analyze_number(list_number)

print(f"minium vaule: {min_value}")
print(f"maximum vaule: {max_value}")
print(f"average vaule: {average_value}")