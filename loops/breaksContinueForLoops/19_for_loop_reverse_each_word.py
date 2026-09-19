"""
Task: Reverse Each Word
Concepts: for loop, string slicing, string concatenation, list

Ask the user for a sentence. Loop through each word and reverse it
individually (not the whole sentence), then print the result as a
new sentence with the words in their original order but each word
reversed.
"""
user_sentence = input("Please provide the sentence to be reversed: ")
sentence_list = user_sentence.split()
reversed_word_list = []
# new_sentence = ""
new_sentence = " ".join(reversed_word_list)

#Loop for reversing the word
for word in sentence_list:
    reversed_wc = ""
    for ch in word:
        reversed_wc = ch + reversed_wc
    reversed_word_list.append(reversed_wc)
#Loop for creating sentence with reversed word list.
# for reversed_word in reversed_word_list:
#     new_sentence += reversed_word + " "
new_sentence = " ".join(reversed_word_list)
print(new_sentence)
