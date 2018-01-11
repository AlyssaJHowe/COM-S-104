def switcheroo(word):
    word = str(word[-1] + word[1:-1] + word[0])
    return word

word = raw_input("Please enter a word: ")
print switcheroo(word)

