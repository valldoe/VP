count:int = int(input())
sum:int = 0

if count <= 0:
    print("въведете число, различно от нула")
    exit

numbers:list = []

for num in range(count):
    num_to_add = int(input())
    sum+=num_to_add

print(sum)