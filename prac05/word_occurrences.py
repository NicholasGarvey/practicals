word_count = {}

text = input("Text: ")
words = text.split()
for word in words:
    try:
        word_count[word] += 1
    except KeyError:
        word_count[word] = 1

words = list(word_count.keys())