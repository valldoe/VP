import random

numbers = [random.randint(1, 50) for num in range(10)]
final = []

print(numbers)

for i in range(len(numbers) - 1):
    final.append(numbers[i])
    final.append(numbers[i] + numbers[i + 1])

final.append(numbers[-1])
print(final)
