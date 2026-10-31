text = input()
chars = {}

for char in text:
    if char != ' ':
        chars[char] = chars.get(char, 0) + 1

print(chars)