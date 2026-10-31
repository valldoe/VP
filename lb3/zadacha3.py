text = input()

chars:dict = {}

for char in text:
    if char in chars:
        chars[char] += 1
    else:
        chars[char] = 1

chars = dict(sorted(chars.items()))

print(chars)