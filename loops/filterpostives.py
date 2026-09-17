import random
# Create a list of numbers (mix of positive, negative, zero). 
# Loop through it and print only the positive numbers, plus a count of how many positives were found.

num_rand = random.sample(range(-45, 51), 10)
print(num_rand)
positive_list = []
count = 0

for n in num_rand:
    if n > 0:
        positive_list.append(n)
        count += 1

print(f"positive list: {positive_list}")
print(f"total positive number in the list: {len(positive_list)}")
