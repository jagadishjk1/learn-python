# Task 1 — Basic List Operations
# Create a list of 5 fruits. Then:
fruits = ['apple', 'banana', 'kiwi', 'orange']

# Print the first and last item (using indexing, including negative indexing for the last one)
print (fruits[0], fruits[-1])

# Add a new fruit to the end using .append()
fruits.append('pineapple')
print(fruits)

# Insert a fruit at position 2 using 
fruits.insert(2, 'berry')
print(fruits)

# Remove one specific fruit using .remove()
# Print the final list
fruits.remove('banana')
print(fruits)