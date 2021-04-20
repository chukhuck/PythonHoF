vowels = ['a', 'o', 'i', 'e', 'u']
word = input("Provide a word to search for vowels: ")

found = {}

for letter in word:
    if letter in vowels:
        found[letter] = found[letter] + 1 if letter in found else 1    


for letter, count in sorted(found.items()):
    print(letter, '-', count)
