num_count = int(input())

num_list = []
sum_even = 0
sum_odd = 0
avg_even:float = 0
avg_odd:float = 0

for i in range(num_count):

    inputed = int(input())
    inputed.append(num_list)

    if inputed == 0:
        print("input is 0")
        continue
    if inputed % 2:
        sum_even += inputed
    if not inputed % 2:
        sum_odd += inputed


print(num_list)
print("sum of the even numbers: " + str(sum_even))
print("sum of the odd numbers: " + str(sum_odd))

print("average of the even numbers: " + str(sum_even / num_count))
print("average of the odd numbers: " + str(sum_odd / num_count))