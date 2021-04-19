vowels = ['a', 'o', 'i', 'e', 'u']
word = input("Provide a word to search for vowels: ")
found_letters = []

for letter in word:
    if letter in vowels and letter not in found_letters:
        found_letters.append(letter)

for letter in found_letters:
    print(letter)
