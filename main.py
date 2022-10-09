with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)

def count_words():
    words = file_contents.split()
    #print(words)
    print(len(words))

count_words()