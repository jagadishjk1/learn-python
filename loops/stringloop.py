# Ask the user for a sentence. Loop through each character in the string.
#count how many vowels (a, e, i, o, u — case-insensitive) it contains.

sentence = input("Enter a letter/sentence you like: ")
case_sentence = sentence.lower()
print(case_sentence)
total_vowels = 0
for letter in case_sentence:
    if letter in ["a", "e", "i", "o", "u"]:
        total_vowels += 1

print(f"Total vowels in given sentence/word: {total_vowels}")