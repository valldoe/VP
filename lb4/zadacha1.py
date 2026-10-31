sentence = input()
words = set(sentence.split())
found_words = []

for word in words:
    if not word in found_words:
        found_words.append(word)

found_words.sort()
print("unique words: " + str(len(found_words)))
print(found_words)
