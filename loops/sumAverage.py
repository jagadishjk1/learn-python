# Create a list of 6 numbers. Using a for loop (no built-in sum()/max()/min() yet — do it manually with a running total and comparisons), calculate and print:

# The sum
# The average
# The largest number
# The smallest number

numbers = [30, 45, 77, 89, 47, 21]
sum_of_numbers = 0
largest = numbers[0]
smallest = numbers[0]

for number in numbers:
   sum_of_numbers = number + sum_of_numbers
   if number > largest:
      largest = number
   if number < smallest:
      smallest = number        

print (sum_of_numbers / len(numbers))
print(f"Largest number: {largest}")
print(f"smallest number: {smallest}")
print(f"sum of numbers = {sum_of_numbers}")