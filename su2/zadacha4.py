n = float(input())
m = float(input())

num_count = 10

num_list = []
sum_numbers_in_range = 0

for i in range(num_count):

    inputed = int(input())
    num_list.append(inputed)

    if n >= inputed <= m:
        sum_numbers_in_range += inputed

print (str(sum_numbers_in_range))