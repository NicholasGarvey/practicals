word_count = {}

text = input("Text: ")
words = text.split()
for word in words:
    try:
        word_count[word] += 1
    except KeyError:
        word_count[word] = 1

words = list(word_count.keys())
words.sort()

maximum_length = max((len(word) for word in words))

for word in words:
    print("{:{}} : {}".format(word, maximum_length, word_count[word]))
