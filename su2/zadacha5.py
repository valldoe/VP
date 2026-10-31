num_count = int(input())
power = int(input())
num_list = []

for i in range(num_count):

    inputed = int(input())
    num_list.append(pow(inputed, power))

print(num_list)