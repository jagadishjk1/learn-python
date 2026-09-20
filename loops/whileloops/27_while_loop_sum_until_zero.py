"""
Task: Sum Until Zero
Concepts: while True, break, accumulator pattern

Keep asking the user to enter numbers, one at a time, adding each
to a running total. Stop when they enter 0, then print the total sum.
"""
number_list = []
zero_point = True


while zero_point:
    print(number_list)
    user_number = int(input("Please Enter your number to sum: "))
    if user_number == 0:
        print("loop Ended, Calculating the sum of given numbers...")
        break
    else:
        number_list.append(user_number)

print(f"Given number by user: {number_list}")
print(f"Sum of given number is: {sum(number_list)}")
