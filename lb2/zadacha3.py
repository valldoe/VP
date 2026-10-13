count:int = int(input())
row:int = 1

if count <= 0:
    print("въведете число, различно от нула")
    exit

for num in range(count):
    print('*' * row)
    row += 1