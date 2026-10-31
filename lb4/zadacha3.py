text = input().split()
num = int(input())

for word in text:
    if len(word) < num:
        text.remove(word)

final = (text)

print(final)
