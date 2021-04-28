# %%
def search4vowels(word: str) -> set():
    """Search vowels in the input word."""
    vowels = 'aeiou'
    found = search4letters(word, vowels)
    return found

def search4letters(phrase:str, letters4search:str) -> set():
    """Search the letters4search in the phrase."""
    found = sorted(list(set(letters4search).intersection(set(phrase))))
    return found

# %%
