n = int(input())

final:dict = {}

for i in range(1, n + 1):
    final[i] = n - i + 1

print(final)