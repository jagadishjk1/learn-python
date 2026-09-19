"""
Task: Longest Word Finder
Concepts: for loop, string methods, comparison (accumulator pattern)

Ask the user for a sentence. Loop through the words and find the
longest one, using the same "running comparison" pattern from the
max/min task earlier (track the longest seen so far as you go).
"""
sentence_input = input("Enter the sentence you want to process: ")
sentence_list = sentence_input.split()

# print(sentence_list)
# print(len(sentence_list[1]))

max_length = 0
longest_word = "" 

for word in sentence_list:  
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

print(f"The longest word in the sentence is: {longest_word} with {max_length} letters.")

