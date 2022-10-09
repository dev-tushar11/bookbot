with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)

def count_words():
    words = file_contents.split()
    #print(words)
    print(len(words))

count_words()

def count_letters():
    letters = {}
    words = file_contents.split()
    for word in words:
        for letter in word.lower():
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] = letters[letter] + 1
    print(letters)

count_letters()