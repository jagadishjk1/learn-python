# Loop through numbers 1 to 20 (use range()). 
# Skip printing any number divisible by 3 using continue, and print all the others.

for number in range(1, 21):
    if number % 3 == 0:
        continue
    print(number)