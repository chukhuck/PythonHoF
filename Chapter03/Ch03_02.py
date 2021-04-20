vowels = set('aeiou')
word = input("Provide a word to search for vowels: ")

print(sorted(list(vowels.intersection(set(word)))))

