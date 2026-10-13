count = int(input())

if count <= 0:
    print("въведете число, различно от нула")
    exit

numbers = []

for num in range(count):
    num_to_add = int(input())
    numbers.append(num_to_add)

for n in numbers:
    print(n)