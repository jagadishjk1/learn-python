"""
Task: Word Frequency (Basic)
Concepts: for loop, string methods, list, dictionary-free counting

Ask the user for a sentence. Count how many times a specific word
(chosen by the user) appears in that sentence, using a for loop.
"""

user_input = input("Please enter your sentence: ")
word_to_search = input("Enter the word you want to count in the sentence: ")
user_input_list = user_input.split()
# print(user_input_list)
wordcount = 0

for word in user_input_list:
    if word.lower() == word_to_search.lower:
        wordcount += 1

print(f"total word count in the sentence is: {wordcount}")
    


