"""
Task: FizzBuzz
Concepts: for loop, if-elif-else, modulo operator

Loop through numbers 1 to 50. 
For multiples of 3, print "Fizz".
For multiples of 5, print "Buzz". 
For multiples of both 3 and 5,
print "FizzBuzz". Otherwise, print the number itself.
"""

for number in range(1,51):
    number_fizz = number % 3
    number_buzz = number % 5
    if number_fizz == 0 and number_buzz == 0:
        print("FizzBuzz")
    elif number_fizz == 0:
        print("Fizz")
    elif number_buzz == 0:
        print("Buzz")
    else:
        print(number)